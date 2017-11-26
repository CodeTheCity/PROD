# PROD (Persuasive Release of Open Data)
A project at [CTC11](http://codethecity.org.uk)

## What is it about?

This project's purpose is building a case for the release of Open Data in Aberdeen. Additionally it explores the  possibilities to automate requests to get the data, if we can't get a portal provided by the Aberdeen City Council.
See [here](http://aberdeen.theodi.org/news-blog/) for the sorry saga. 

This part covers the automation of requests to [WhatDoTheyKnow](http://whatdotheyknow.com) a site which makes easier, and allows tracking of, the submission of FOI requests. 

## Approach

We will use the what do they know API to create requests on the fly: https://www.whatdotheyknow.com/help/api

And there as some helpful hints (on which we based this) [here](https://www.mysociety.org/2016/12/19/alaveteli-for-campaigners-how-to-create-pre-written-requests-for-your-supporters/?refferer=mailnotify&uid=138 )

I have adapted these instructions to those below. 

But none of them have used selenium to automate the process which was my aim.

## Method for creating requests on the fly

1. It’s quite simple to create yourself. Just build the URL up in steps:

The base URL: https://www.whatdotheyknow.com/

2. Begin by telling the site that this is a new request: https://www.whatdotheyknow.com/new/

3. Add a forward slash (/) and then the body you want the request to be sent to (exactly as it is written in the url of the body’s page of the website): https://www.whatdotheyknow.com/new/aberdeen_city_council

4. Add a question mark: This tells the website that we are going to introduce a ‘parameter string’. Now our URL looks like this: https://www.whatdotheyknow.com/new/aberdeen_city_council?

5. Input a title: we need to indicate that the next part should go into the ‘title’ field, like this: 
https://www.whatdotheyknow.com/new/aberdeen_city_council?title= 
and then indicate what the title should be, thus: 
https://www.whatdotheyknow.com/new/aberdeen_city_council?title=EV%20Charging%20Points

Notice that if there is a space between words, it should be shown as %20. To make the process of encoding the URLs easier, you can use an encoder tool like this one: https://meyerweb.com/eric/tools/dencoder/ In my code I have used the Python library to encode the URL string ( from urllib.parse import urlencode )

6. Input the body of the request, again using ‘%20’ between each word. This is where your URL can become very long! We use the parameter "default_letter"

The salutation (Dear…) and signoff (Yours…) are automatically wrapped around this by the site, so there’s no need to include them:

https://www.whatdotheyknow.com/new/aberdeen_city_council?title=EV%20Charging%20Points&default_letter=

7. Then add the text of the request. In our example, "geo-located list of charging points for electrical vehicles along with a note of the frequency of the update of this data set (e.g. Monthly, Quarterly, Annually)" becomes this when encoded: 

a%20geo-located%20list%20of%20charging%20points%20for%20electrical%20vehicles%2C%20along%20with%20a%20note%20of%20the%20frequency%20of%20the%20update%20of%20this%20data%20set%20(e.g.%20Monthly%2C%20Quarterly%2C%20Annually)

8. So, stringing these all together we get:
https://www.whatdotheyknow.com/new/aberdeen_city_council?title=EV%20Charging%20Points&default_letter=a%20geo-located%20list%20of%20charging%20points%20for%20electrical%20vehicles%2C%20along%20with%20a%20note%20of%20the%20frequency%20of%20the%20update%20of%20this%20data%20set%20(e.g.%20Monthly%2C%20Quarterly%2C%20Annually)


9. Finally we can use tags. This allows you to add a space-separated list of tags, so for example you can identify any requests made through your campaign or which refer to the same topic. 

So, we can add "&tags=ODIAberden%20CTC11" which will tag the request ODIAberdeen and CTC11.

10. The final URL we end up with is:

https://www.whatdotheyknow.com/new/aberdeen_city_council?title=EV%20Charging%20Points&default_letter=a%20geo-located%20list%20of%20charging%20points%20for%20electrical%20vehicles%2C%20along%20with%20a%20note%20of%20the%20frequency%20of%20the%20update%20of%20this%20data%20set%20(e.g.%20Monthly%2C%20Quarterly%2C%20Annually)&tags=ODIAberden%20CTC11

## What about selenium?

To be added