from doggies.models import Breed
import csv

from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def load_breeds(self):
        with open('doggies/management/commands/doggie_data.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            # line_count = 0
            for row in csv_reader:
                # if line_count == 0:
                #     print(f'Column names are {", ".join(row)}')
                #     line_count += 1
                # else:
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                if row[0] == "Name":
                    continue

                my_name = row[0]
                # print(my_name)
                my_size = row[1]
                # print(my_size)
                my_kid_friendly = row[2]
                # print(my_kid_friendly)
                my_dog_friendly = row[3]
                # print(my_dog_friendly)
                my_low_shedding = row[4]
                # print(my_low_shedding)
                my_easy_to_groom = row[5]
                # print(my_easy_to_groom)
                my_high_energy = row[6]
                # print(my_high_energy)
                my_good_health = row[7]
                # print(my_good_health)
                my_low_barking = row[8]
                # print(my_low_barking)
                my_intelligence = row[9]
                # print(my_intelligence)
                my_easy_to_train = row[10]
                # print(my_easy_to_train)
                my_tolerates_hot = row[11]
                # print(my_tolerates_hot)
                my_tolerates_cold = row[12]
                # print(my_tolerates_cold)
                b = Breed(name=my_name, size=my_size, kid_friendly=my_kid_friendly, dog_friendly=my_dog_friendly,
                low_shedding=my_low_shedding, easy_to_groom=my_easy_to_groom, high_energy=my_high_energy,
                good_health=my_good_health, low_barking=my_low_barking, intelligence=my_intelligence,
                easy_to_train=my_easy_to_train, tolerates_hot=my_tolerates_hot, tolerates_cold=my_tolerates_cold)
                # print(b.size)
                b.save()
                # break
            # print(f'Processed {line_count} lines.')

    def handle(self, *args, **options):
        self.load_breeds()
