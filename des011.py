larg = float(input('largura da parede:' ))
alt = float(input('Altura da parede:' ))
área = larg * alt
print('Sua parede tem a dimensão de {} x {} e sua área é de {} m2.'.format(larg, alt, área))
tinta = área / 2
print('Para pintar sua parede você precisará de {}l de tinta'.format(tinta))

