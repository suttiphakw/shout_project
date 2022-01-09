def shouter_interest(interest_list):
  interest = []
  for foo in interest_list:
    if foo == 'technology_gadget':
      interest.append('📱Technology & Gadget')
    elif foo == 'social_csr':
      interest.append('⭐️ Social & CSR')
    elif foo == 'entertainment':
      interest.append('🎸 Entertainment')
    elif foo == 'finance_investment':
      interest.append('💰 Finance & Investment')
    elif foo == 'lifestyle':
      interest.append('🌻 Lifestyle')
    elif foo == 'fashion':
      interest.append('👗 Fashion')
    elif foo == 'automobile':
      interest.append('🚘 Automobile')
    elif foo == 'food_drink':
      interest.append('🍔 Food & Drink')
    elif foo == 'beauty':
      interest.append('💄 Beauty')
    elif foo == 'travel':
      interest.append('✈️ Travel')
    elif foo == 'health_sport':
      interest.append('🏀 Health & Sport')
    elif foo == 'design_art':
      interest.append('🎨 Design & Art')
    elif foo == 'luxury':
      interest.append('👜 Luxury')
    else:
      continue

  return interest
