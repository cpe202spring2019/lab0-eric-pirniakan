def weight_on_planets():
    weight = int(input('What do you weigh on earth? '))
    
    mars_weight = weight*0.38
    jupiter_weight = weight*2.34
    
    print('\nOn Mars you would weigh', mars_weight, 'pounds.\nOn Jupiter you would weigh', jupiter_weight, 'pounds.')
    
if __name__ == '__main__':
    weight_on_planets()
