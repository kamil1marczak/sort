package com.sort;
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.logging.Logger;

import java.text.SimpleDateFormat;
import java.util.Date;

import java.util.logging.Formatter;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.LogRecord;

public class Bubble {

    static Logger logger = Logger.getLogger(Bubble.class.getName());

    private static int sizeOfList = 10000;

    public static void main(String[] args) {

        long firstTimeStamp = System.currentTimeMillis();

        logger.info("start");

        RawList r = new RawList(sizeOfList);
        int rawList[] = r.getRawList();

        long secondTimeStamp = System.currentTimeMillis();
        long diffImport = secondTimeStamp - firstTimeStamp;

        logger.info("difference: "+diffImport);

        int checkList = 0;

        while (checkList < sizeOfList) {

//            for (int i = 0; i < sizeOfList; i++) {
//                System.out.print(rawList[i] + " ");
//            }
//            System.out.println();

            for (int j = 0; j < sizeOfList - 1; j++) {
                if (rawList[j] <= rawList[j + 1]) {
                    checkList += 1;
                } else {
                    checkList = 0;
                    for (int i = j; i < sizeOfList - 1; i++) {
                        if (rawList[i] > rawList[i + 1]) {
                            int tmp = rawList[i];
                            rawList[i] = rawList[i + 1];
                            rawList[i + 1] = tmp;
                        }

                    }
                }


            }
        }

        long thirdTimeStamp = System.currentTimeMillis();
        long diffSort = thirdTimeStamp - secondTimeStamp;

        logger.info("difference: "+diffSort);

        String arrayAsString = Arrays.toString(rawList);
        System.out.println(arrayAsString);

    }

}

