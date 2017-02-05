# Distributed Computing - Part 1
In this lab we will be doing data processing with data from AWS S3. A small rest API has been provided to you. Your job is to implement one function that API needs to call to find the average census tract population size for a given city. The goal of this lab is to set up for part two, where we will run this API on a cluster of multiple machines to increase performance.

## The REST API
This API only has two endpoints. The / endpoint just returns a string saying "Welcome to lab!"
The second endpoint is documented as follows

    /average_pop?city

        city: name of a US city. Can be one of
            `baltimore`, `charelston`, `chicago`, `columbus`, `dayton`, `denver`,
            `kc`, `memphis`, `milwaukee`, `ok_city`, `pittsburg`, `st_louis`,
            `syracuse`, or `wichita`
