import asyncio
import websockets

with open('prog_physic_db.txt', 'r') as f:
    reference = f.readlines()

with open("cas_number_db.txt", 'r') as f:
    reference_cas = f.readlines()


def andler(text):

    text = text.replace("Yo, please tell me what is the value of the ", '')
    text = text.replace("Can you tell me what is the ", '')

    text = text.replace(" please?", '')

    if "atomic weight" in text:
        text = text.replace("atomic weight of ", '')
        text = text.replace("atomic weight for the ", '')
        text = text.replace(' ', '')
        print("Detected atom :", text)
        for line in reference:
            if text in line:
                if "[" in line:
                    answer = line[line.index("["):line.index("]")]
                else:
                    answer = line[line.index(".")-3:line.index("(")]
                answer = answer.replace('\t', '').lower()
                answer = answer.replace(' ', '')
                answer = answer.replace("[", '')
                
                if "." in answer:
                    return str(round(float(answer),1))
                else:
                    return answer


    elif "cas number" in text:
        text = text.replace("cas number of ", '')
        text = text.replace("cas number for the ", '')
        text = text.replace(' ', '')
        print("Detected atom :", text)
        for line in reference_cas:
            if text in line:
                if '\t' in line:
                    answer = line.split('\t')[1]
                else:
                    answer = line.split(' ')[1]
                answer = answer.replace('\t', '').lower()
                answer = answer.replace(' ', '')

                return answer.replace('\n', '').upper().replace("CAS", '')

    elif "number of electrons" in text:
        text = text.replace("number of electrons of", '')
        text = text.replace("number of electrons for the", '')
        text = text.replace(' ', '')
        print("Detected atom :", text)
        for line in reference:
            if text in line:
                answer = line.lower().split(text.lower())[0]
                answer = answer.replace(" ", '')

                return str(int(answer))


async def main():
    async with websockets.connect('ws://ctf10k.root-me.org:8000') as websocket:
        while True:


            response = await websocket.recv()

            octet = ""
            total = ""
            for bit in response:
                octet += bit
                if len(octet) >= 8:
                    total += chr(int(octet, 2))
                    octet = ""

            print("Question : ")
            print(total)
            reponse = andler(total)
            print("Sending :", reponse)

            
            binary_resp = ""
            for l in reponse:
                binary_resp += "0"*(10-len(bin(ord(l)))) + bin(ord(l)).replace('0b', '')


            await websocket.send(binary_resp)
            
            await websocket.recv()





asyncio.get_event_loop().run_until_complete(main())


flag = "RM{4t0ms_sp33drunn3r_sp3c14l1st}"