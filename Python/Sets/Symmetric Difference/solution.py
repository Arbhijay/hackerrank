#!/usr/bin/env python3

# -*- coding:utf-8 -*-
# @Script: solution.py
# @Author: Pradip Patil
# @Contact: @pradip__patil
# @Created: 2018-02-18 20:56:23
# @Last Modified By: Pradip Patil
# @Last Modified: 2018-02-19 21:43:06
# @Description: https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    m = int(input())
    M = set(input().split())
    n = int(input())
    N= set(input().split())

    print("\n".join(sorted(M^N, key=int)))
