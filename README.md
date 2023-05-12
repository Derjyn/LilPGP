# LilPGP
A super-simple Python script with PGP functionality, engineered utilizing ChatGPT.

![image](https://github.com/Derjyn/LilPGP/assets/648059/ac4c3527-b17d-48fa-a720-a8241418c297)

<br/><br/>
 
<details>
<summary>Prerequisites</summary>

### Prerequisites
This script is Python based, so make sure that you have Python installed and accessible. Outside of this, you will want some sort of PGP key/certificate manager. A good quick solution is to install Gpg4win. It's open-source, and includes Kleopatra for managing keys/certificates. You can download Gpg4win here: https://www.gpg4win.org/

Finally, make sure you have *tkinter* and *gnupg* libraries installed before running the script. Run this install command from a terminal:

```
pip install tkinter gnupg
```
</details>

<details>
<summary>Usage</summary>

### Usage
There are 4 main functions in LilPGP:
  1. Creating secret keys.
  2. Exporting public keys based on a list of available secret keys.
  3. Encrypting a directory of files based on a selected public key.
  4. Decrypting a file, so long as the associate secret key is available and valid.

<br/>
  
**Creating a secret key**

![image](https://github.com/Derjyn/LilPGP/assets/648059/fc283992-a30f-47fa-92d7-e33d3cdd21f6)
  
To create a secret key, simply fill in the fields in the *Create secret key* section, and hit the *Create Key* button. This (*should*) create a secret key on your system, and refresh the list of available secret keys in the *Export public key* section.

<br/>

**Exporting a public key**

![image](https://github.com/Derjyn/LilPGP/assets/648059/9b3aa0d6-049f-48b8-ad89-54af30462a9d)

To export a public key (*for use in encrypting files*), select a valid secret key from the list of available keys. Then hit the *Export Key* button.

<br/>
  
**Encrypting files using a public key**

![image](https://github.com/Derjyn/LilPGP/assets/648059/8ba3ef81-6fdd-4ada-97c1-888fdb55f22a)

In order to encrypt a directory of files, you'll first need to select a valid public key. This key should be paired with a secret key that is available on the specified system that would wish to later decrypt these files. For example, here the *john_doe_PUBLIC.asc* key has been selected, which was exported using the approach in the previous step:
 
![image](https://github.com/Derjyn/LilPGP/assets/648059/e02fd940-7e34-4ed2-aa82-c0fc05c465b5)

Now that this public key has been selected, a directory of files can be encrypted. For testing purposes, this repository contains a directory with 3 text files:
  * test_dir
    * test_file_a.txt
    * test_file_b.txt
    * test_file_c.txt
  
This directory will be selected, using the *Select Directory* button, and then encrypted using the *Encrypt Directory* button. Once the encryption process complete a new directory will have been created (named *encrypted*), with the 3 test files encrypted and named with the *.gpg extension.

![image](https://github.com/Derjyn/LilPGP/assets/648059/4d80459a-814d-4763-a6ed-9a563e93e814)

![image](https://github.com/Derjyn/LilPGP/assets/648059/5fff5a33-f575-4855-9444-5fcb6fd4f5c8)

<br/>
  
**Decrypting files**

Decrypting a directory of previously encrypted files is easier than encrypting. The only caveat is that the secret key associated with the public key utilized to encrypt the files must be present on the system. Once this requirement is secured, hit the *Select Directory* button, this time making sure to select the directory with the encrypted files (*in this case, 'encrypted'*).
  
Once the correct directory is selected, hitting the *Decrypt Directory* button will begin the decryption process - but first a passphrase prompt will pop up. Enter in the passphrase associated with the secret/public key, and hit okay. If the associated passphrase has previously been entered, it may not be necessary to enter the passphrase again. This is a potential security improvement that can be made in LilPGP's future.
  
![image](https://github.com/Derjyn/LilPGP/assets/648059/41d30a37-d122-4b5f-90d7-3229a097d60e)

Once complete, a new directory (*decrypted*) will have been created, containing the now encrypted files.
  
![image](https://github.com/Derjyn/LilPGP/assets/648059/42d5f862-f194-4ad4-8210-c6826ef6e8b7)

![image](https://github.com/Derjyn/LilPGP/assets/648059/8bf8a3f5-2ad1-4706-a97f-9020003a63a0)

</details>

<details>
<summary>Improvements</summary>

### Improvements
  
Through the rapid development of LilPGP, some potential improvements were identified:
  
  * More robust error checking and handling
  * Input validation
  * File overwrite prevention
  * Logging (*file logging, versus message output within the GUI*)
  * Security enhancements
  
Future iterations of LilPGP could also tune up the GUI a bit, integrating a more modern UI and features such as tooltips. All-in-all, for a script created within a couple of hours, it's not so bad! It does what it was intended to do and within local testing environments, seems to be error free. Of course this is likely to fall apart once it is tested on external systems...

</details>
