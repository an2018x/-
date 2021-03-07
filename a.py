import paddlehub as hub

module=hub.Module(name="lac")



inputs = {"text": ["长扬汽车修理厂"]}
results = module.lexical_analysis(data=inputs)

with open('out.txt','w') as f:
    for result in results:
        print(result)
        #f.write(result)

