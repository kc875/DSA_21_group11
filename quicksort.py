import time
import os
import sys
import random
import numpy as np

sys.setrecursionlimit(10**6)
print_arrays = False  # boolean to determine whether to print out the original and sorted arrays
quick_count = 0  # count for number of comparisons for quicksort (insertion sort compares count)
cutoff = 3  # cutoff size for subarrays until quicksort switches to insertion sort
# note that the cutoff will never be less than 2 even if this value is changed to less than 2


# each value in the array should be in a different line

# helper function
def parse_file(file):
	# check to see if the path is valid
	if not os.path.exists(file):
		print("ERROR: File does not exist!")
		sys.exit(-1)

	no_list = []
	with open(file, "r") as fd:
		for line in fd:
			no_list.append(int(line.rstrip("\n")))
	fd.close()
	# returning the created list
	return no_list


def insertion_sort(arr):
	global quick_count
	for i in range(1, len(arr)):
		j = i - 1
		while j >= 0 and arr[j + 1] < arr[j]:
			quick_count = quick_count + 1  # count for number of comparisons for quicksort
			tmp = arr[j]
			arr[j] = arr[j + 1]
			arr[j + 1] = tmp
			j = j - 1
	return arr


def select_pivot(arr, p_type):
	# type = 0 --> first element
	# type = 1 --> median of three
	# else --> random
	low = []
	high = []
	if p_type == 0:
		pivot = arr.pop(0)
		return [arr, pivot, low, high]
	elif p_type == 1:
		l = 0
		r = len(arr)
		m = (l + r) // 2  # midpoint

		tmp = []  # temporary array for sorting the three possible pivot values
		m_element = arr.pop(m)  # removing the midpoint of the array
		tmp.append(m_element)
		l_element = arr.pop(0)  # removing the first element of the array
		if l_element < m_element:
			tmp.insert(0, l_element)
		else:
			tmp.append(l_element)
		r_element = arr.pop(len(arr) - 1)  # removing the last element of the array
		if r_element < tmp[0]:
			tmp.insert(0, r_element)
		elif r_element < tmp[1]:
			tmp.insert(1, r_element)
		else:
			tmp.append(r_element)

		# since the possible pivot values were inserted so that the array was sorted,
		high.append(tmp.pop())  # the last value is greater than the chosen pivot
		low.append(tmp.pop(0))  # the first value is less than the chosen pivot
		pivot = tmp.pop()  # the middle value (last one in the array now) is the pivot

		return [arr, pivot, low, high]
	else:
		pivot = arr.pop(random.randint(0, len(arr) - 1))
		return [arr, pivot, low, high]


def partition(arr, type):
	global cutoff  # cutoff size for switching to insertion sort
	global quick_count  # count for number of comparisons for quicksort
	part = [] # array to be returned and to contain the array and the pivot value's index
	low = []  # array of values less than the pivot
	high = []  # array of values greater than the pivot
	if len(arr) <= max(2, cutoff):  # if the size of the array is less than the cutoff value, do insertion sort
		arr = insertion_sort(arr)
		part.append(arr)
		return part

	p = select_pivot(arr, type)
	arr = p.pop(0)
	pivot = p.pop(0)
	low = p.pop(0)
	high = p.pop(0)

	for item in arr:  # iterate throught the remaining items in the array + place them in appropriate low or high array
		quick_count = quick_count + 1
		if item <= pivot:
			low.append(item)
		else:
			high.append(item)

	return [low, [pivot], high]

def flatten(list):
	output = []
	for i in list:
		output.extend(i)
	return output

def quicksort(arr, type):
	s1 = [arr]
	s2 = []
	sorted = False
	while not sorted:
		sorted = True
		for a in s1:
			if len(a) == 0:
				continue
			elif len(a) == 1:
				s2.append(a)
				continue
			if len(a) > 3:
				sorted = False
			s2.extend(partition(a, type))

		s1 = s2.copy()
		s2 = []

	return flatten(s1)


def quicksort_from_file(filename, sort_type):
	# print("---QuickSort---")
	a = parse_file(filename)
	if print_arrays:
		print(a)
	global quick_count
	quick_count = 0
	start = time.perf_counter()
	a_sorted = quicksort(a, sort_type)
	end = time.perf_counter()
	if print_arrays:
		print(a_sorted)
	# print("Number of Comparisions: {}".format(quick_count))
	quick_time = (end - start) * 1000
	# print("Time Taken: {} ms".format(quick_time))
	return quick_count, quick_time

def main():
	ft_0 = open("times_firstElement.txt", "x")
	fc_0 = open("counts_firstElement.txt", "x")
	ft_1 = open("times_median.txt", "x")
	fc_1 = open("counts_median.txt", "x")
	ft_2 = open("times_random.txt", "x")
	fc_2 = open("counts_random.txt", "x")

	ft_0.write("count, mean, std\n")
	fc_0.write("count, mean, std\n")
	ft_1.write("count, mean, std\n")
	fc_1.write("count, mean, std\n")
	ft_2.write("count, mean, std\n")
	fc_2.write("count, mean, std\n")

	sizes = [8, 64, 256, 512, 1024, 4096, 8192, 32768, 1048576, 33554432]
	for size in sizes:
		files = []
		print(f"---Size {size}---")
		for i in range(1, 11):
			files.append(f"./Data/Random/{size}/random{size}_{i}.txt")
		for i in range(3):
			counts = []
			times = []
			if i == 0:
				print("---FIRST ELEMENT PIVOT---")
			elif i == 1:
				print("---MEDIAN OF THREE---")
			elif i == 2:
				print("---RANDOM---")
			for f in files:
				c, t = quicksort_from_file(f, i)
				counts.append(c)
				times.append(round(t, 4))
			print(f"Counts: {counts}")
			print(f"Times: {times}")
			if i == 0:
				ft_0.write(f"{size}, {np.mean(times)}, {np.std(times)}\n")
				fc_0.write(f"{size}, {np.mean(counts)}, {np.std(counts)}\n")
				ft_0.flush()
				fc_0.flush()
			elif i == 1:
				ft_1.write(f"{size}, {np.mean(times)}, {np.std(times)}\n")
				fc_1.write(f"{size}, {np.mean(counts)}, {np.std(counts)}\n")
				ft_1.flush()
				fc_1.flush()
			elif i == 2:
				ft_2.write(f"{size}, {np.mean(times)}, {np.std(times)}\n")
				fc_2.write(f"{size}, {np.mean(counts)}, {np.std(counts)}\n")
				ft_2.flush()
				fc_2.flush()


if __name__ == '__main__':
	main()