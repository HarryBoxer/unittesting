## Tests for countUnique

| Test case                             |  Expected Result   |
|---------------------------------------|--------------------|
| empty list                            | return 0           |
| one unique                            | return 1           |
| two uniques                           | return 2           |
| three uniques                         | return 3           |
| one alphabet with upper and lowercase | return 2           |
| two alphabet with upper and lowercase | return 4           |



## Tests for searchBinary

| Test case                             |  Expected Result                             |
|---------------------------------------|----------------------------------------------|
| empty list                            | return -1                                    |
| normal searches                       | return index                                 |
| duplicate element odd amount          | return middle one                            |
| duplicate element even amount         | return most close to the middle one from less|
| None                                  | return Raises TypeError                      |
| element not available                 | return -1                                    |


