#A simple sepolicy denial resolver that will read your denials from a file and resolves and puts them in the respective files.
#TODO
Categorization as to public/private/vendor etc.(If someone can help me with on what basis it's done)

#HowTo Use
1) from your log create a denials.txt file with only denial
   If on linux you can use this:
   
   ```
   cat PATH_TO_LOG.txt | grep avc: > denials.txt
   ```
2) Put the denials.txt in your device tree.
3) Run this code in the root folder of your device tree.

All your denials should be resolved:)
Any suggestions would be appreciated and helpful.
