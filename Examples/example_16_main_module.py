import myfunction as f

# interpreter sets __name__ to "__main__" in main method
print(f'__name__ in myfunction is {__name__}')

if __name__=="__main__":
    # inside imported method __name__ is set to method name; inside myfunction method __name__ will be set to myfunction
    area = f.rectangle_area(12,5)
    print(area)

