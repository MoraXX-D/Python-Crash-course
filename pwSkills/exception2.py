import logging

try:
    logging.basicConfig(filename='exception.log', level= logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    with open("name2.txt",'r') as f:
        # f.write("John")
        data = f.read()
        logging.info(data)
except Exception as e:
    logging.error(f"An error occurred: {e}")  # Corrected logging format
else:
    f.close()
    logging.info('added to file and file closed')
finally:
    logging.info('exception handled')