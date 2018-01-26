def centuryFromYear(year):
    if year < 100:
        century=1;
        print(century);
        return(century);
    elif year > 100:
        century=year/100;
        if century==int(century):
            print(century);
            return(century);
        print(int(century)+1);
        century=(int(century)+1);
        return(century);
