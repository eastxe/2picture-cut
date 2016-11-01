#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import random
import itertools

import numpy as np
import cv2


class CutSamePicture():
    def __init__(self):
        pass

    def cut(self):
        self.entire_img_path = './hukei.png'
        self.img_path = './hukei_t.png'
        self._input_pictures()
        self._extraction_array()
        self._search()

    def _input_pictures(self):
        '''
        search_img is what you want to search same image
        entire_image is an entire image what is in  search_img image
        '''
        self.entire_img = cv2.imread(self.entire_img_path)
        self.search_img = cv2.imread(self.img_path)

    def _path_conversion(self):
        pass

    def _check(self):
        for pos in itertools.product(range(10), range(10)):
            if (self.search_Mat[pos[0]][pos[1]] ==
                    np.array([255, 255, 255])).all():
                break
            else:
                return True
        return False

    def _extraction_array(self):
        left, top = 0, 0
        down, right = self.search_img.shape[:2]
        if right - left < 10 or down - top < 10:
            print 'inputed image is too small'
            raise
        for _ in xrange(100):
            x = random.randint(int(right * 1 / 3), int(right * 2 / 3))
            y = random.randint(int(down * 1 / 3), int(down * 2 / 3))
            self.search_Mat = self.search_img[y:y + 10, x:x + 10]
            if self._check():
                self.pos_x = x
                self.pos_y = y
                break
        else:
            print 'sorry, I did not find a good image for this search'
            raise

    def _search(self):
        down, right = self.entire_img.shape[:2]
        for pos in itertools.product(range(down - 10), range(right - 10)):
            print pos
            target = self.entire_img[pos[0]:pos[0] + 10, pos[1]:pos[1] + 10]
            if np.array_equal(self.search_Mat, target):
                break
        else:
            print 'sorry, we cannot find the same image'
            raise
        result_img = self.entire_img[pos[0] - self.pos_y:pos[0] -
                self.pos_y + self.search_img.shape[0],
                pos[1] - self.pos_x:pos[1] - self.pos_x + self.search_img.shape[1]]
        # cv2.imwrite('result.png', result_img)
        cv2.imshow('result', result_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    I = CutSamePicture()
    I.cut()
