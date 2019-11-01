A simple sepolicy denial resolver that will read your denials from a file and resolves and puts them in the respective files.

On basis of my understanding i have done the separation as follows:

	system/sepolicy/private in sepolicy/private

	system/sepolicy/vendor  in sepolicy/vendor

	Remaining  in sepolicy/public

The list for the same has been created using the categ.py pressent in the git

#HowTo Use
1) from your log create a denials.txt file with only denial
   If on linux you can use this:
   
   ```
   cat PATH_TO_LOG.txt | grep avc: > denials.txt
   ```
2) Put the denials.txt in your device tree.
3) If treble device Place sepwriter_v.py in the folder of your dtree.
4) Run the code by executing the following command:
   ```
   python3 sepwriter_v.py
   ```

(or)

3) If non treble Place sepwriter.py in the folder of your dtree.
4) Run the code by executing the following command:
   ```
   python3 sepwriter.py
   ```

(or)
3) If your device tree doesnt have folders like sepolicy/public sepolicy/private etc copy the sepwriter_simple.py in the folder of your dtree.
4) Run the code by executing the following command:
   ```
   python3 sepwriter_simple.py
   ```
All your denials should be resolved:)

An example of how the code resolves your denials is provided in dtree folder.(Check Readme there for further info)

Any suggestions would be appreciated and helpful.
