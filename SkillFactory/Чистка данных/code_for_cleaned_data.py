def outliers_iqr(data,feature):
    x=data[feature]
    quartile_1,quartile_3=x.quantile(0.25),x.quantile(0.75)
    iqr=quartile_3-quartile_1
    lower_bound=quartile_1-(iqr*1.5)
    upper_bound=quartile_3+(iqr*1.5)
    
    outliers=data[x<lower_bound|x>upper_bound]
    cleaned=data[x>=lower_bound&x<=upper_bound]
    return outliers,cleaned

if __name__ == '__main__':
    outliers_iqr()