package com.sort;

import java.util.Random;

public class RawList {

    private int[] rawList;

    public RawList(int n) {


        Random randomGenerator = new Random(); // pseudo random
//        randomGenerator.nextInt(100);

        rawList = new int[n];

        for (int i = 0; i < n ; i++) {
            rawList[i] = randomGenerator.nextInt();
        }
    }

    public int[] getRawList() {
        return rawList;
    }


}

// classes, interfaces, overloadin, overriding (inheritance), static elements, loops while dowhile, foreach, | switch,

// static, class - jvm memory model, class loaders, garbage collection