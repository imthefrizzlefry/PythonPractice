'''This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. 
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. 
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.
'''

def find_longest_absolute_path(directory_struture):
    cur_absolute_path = []
    longest_path = ""

    for line in directory_struture.split('\n'):
        path_levels = line.split('\t')

        if len(cur_absolute_path) < len(path_levels):
            cur_absolute_path.append(path_levels[-1])
        elif len(cur_absolute_path) == len(path_levels):
            cur_absolute_path[-1] = path_levels[-1]
        else:
            cur_absolute_path = cur_absolute_path[:len(path_levels)]
            cur_absolute_path[-1] = path_levels[-1]

        if '.' in  cur_absolute_path[-1]:
            cur_path = "/".join(cur_absolute_path)
            longest_path = cur_path if len(cur_path) > len(longest_path) else longest_path

    return longest_path

        



if __name__ == "__main__":
    list_of_inputs = [
        #("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext","dir/subdir2/file.ext"),
        ("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext","dir/subdir2/subsubdir2/file2.ext")]

    for input in list_of_inputs:

        print(input[0])

        longest = find_longest_absolute_path(input[0])

        print(longest)

        assert longest == input[1]
