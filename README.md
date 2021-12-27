# AES and RSA Program 
#### Author: Sixin Li 
### Background
AES and RSA are two cryptographical methods.

As of 2021, AES is the most widely used file encryption method mainly because of its speed in dealing with large files. But it distributes the same key for both senders and receivers, which makes it unsafe in the management of keys. It is hence called symmetric encryption method.
</br></br>
On the other hand, RSA is an asymmetric encryption method which keeps a public 
key for senders and keeps a private key for each receiver. As long as the length of the keys are long enough, it is almost impossible to break. It is safe in terms of management but is usually slow in speed.

### Description
This project is mainly used to display the time difference of message encryption using the AES and RSA method. It implements RSA using Python following the regular mathematical methods in the below list, and implements AES using existing Python modules.

>Not using existing RSA module here is to display the whole building process detailedly

- Select two large prime numbers, p and q
  - Miller-Rabin algorithm
- Compute N = pq and φ(N) = (p-1) * (q-1) 
- Find an integer e such that gcd(e, φ(N)) = 1
- Compute the multiplicative inverse of e mod φ(N) : an integer d such that (ed mod φ(N) ) = 1
  - Extended Euler’s Theorem
- Display public(encryption) key: N and e
- Display private (decryption) key: d

### Program GUI
![image](https://user-images.githubusercontent.com/45926850/147425972-b35927be-03bb-4d44-a794-c64c7fafb98f.png)


### User Guide
1. Run Main.app
2. Click "512"/"1024" button on the right to generate keys each with 512/1024 bits.
3. Click the RSA button on the lower part. 
4. Click the AES button on the side.
5. The table below shows the time(in microseconds) spent to encrypt messages in three text files.
