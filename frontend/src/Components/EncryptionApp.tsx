import React, { useState, useContext } from "react";
import { EncryptionContext } from "../Context/EncryptionContext";
import styles from "./EncryptionApp.module.css";

export const EncryptionApp = () => {
  const {
    error,
    encryptionText,
    decryptionText,
    setDecryptionText,
    encryptionKey,
    setEncryptionKey,
    decryptionKey,
    setDecryptionKey,
    encryptionMethod,
    setEncryptionAlgorithm,
    encryptText,
    decryptText,
  } = useContext(EncryptionContext);

  const [inputEncrypt, setInputEncrypt] = useState("");
  const [inputDecrypt, setInputDecrypt] = useState("");
  
  const [copied,setCopied] = useState(false);
  const handleCopy = (text:string) => {
    navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => {setCopied(false)}, 1500);
  }

  const handleEncrypt = async () => {
    console.log("encrypt")
    if (encryptionMethod != "RSA" && (!inputEncrypt || !encryptionKey)){
      alert("Please enter text and encryption key !");
      return;
    }
    await encryptText({ text: inputEncrypt });
  };

  const handleDecrypt = async () => {
    if(encryptionMethod != "RSA" && (!inputDecrypt || !decryptionKey)){
      alert("Please enter encrypted and decryption key !");
      return;
    }
    else if(encryptionMethod != "RSA" && encryptionKey != decryptionKey){
      alert("please enter the correct decryption key");
      return;
    }
    await decryptText({ text: inputDecrypt });
    setTimeout(() => {setDecryptionText("")},1500);
    
  }
  return (
    <div className={styles.container}>
      <h1 className={styles.welcome}>WELCOME TO ENCRYPTION ENVIRONMENT </h1>
      <div className={styles.main}>
        <div className={styles.encrypt}>
          <h1 >
            Message to Encrypt
          </h1>
          <input
            type="text"
            placeholder="Enter text to encrypt"
            value={inputEncrypt}
            onChange={(e) => setInputEncrypt(e.target.value)}
          />
        </div>
        <div className={styles.decrypt}>
          <h1>Message to Decrypt</h1>
          <input type="text" placeholder="Enter text to decrypt" value={inputDecrypt} onChange={(e) => setInputDecrypt(e.target.value)}/>
        </div>
      </div>
      <div className={styles.key}>
      <div className={styles.keyfield}>
          <p>Encryption Key</p>
          <input type="text" placeholder="Encryption Key" value={encryptionKey} onChange={(e: React.ChangeEvent<HTMLInputElement>) => setEncryptionKey(e.target.value)} />
        </div>
        <div className={styles.keyfield}>
          <p>Decryption Key</p>
          <input type="text" placeholder="Decryption Key" value={decryptionKey}  onChange={(e: React.ChangeEvent<HTMLInputElement>) => setDecryptionKey(e.target.value)}/>
        </div>
      </div>
      <div className= {styles.btn}>
        <div className={styles.rightbtn}>
           <button onClick={handleEncrypt}>Encrypt</button>
           <button onClick={() => handleCopy(encryptionText)} className={styles.btn2}>{copied ? "Copied":"Copy Encrypt"}</button>
        </div>

        <div className={styles.leftbtn}>
           <button onClick={handleDecrypt}>Decrypt</button>
           <button onClick={() => handleCopy(decryptionText)} className={styles.btn2}>{copied ? "Copied":"Copy Decrypt"}</button>
        </div>

      </div>
      <div className={styles.output}>
        <div className={styles.output1}>
            <input type="text" placeholder="encrypted text" value={encryptionText} readOnly/>
        </div>
        <div className={styles.output2}>
            <input type="text" placeholder="decrypted text" value={decryptionText} readOnly />
            {error && <p className={styles.error}>{error}</p>}
        </div>
      </div>
      <div className={styles.select}>
        <label className={styles.label}>Choose Algorithm:</label>
        <select value={encryptionMethod} onChange={(e) => setEncryptionAlgorithm(e.target.value)}>
          <option value={""}>...</option>
          <option value="RSA">RSA</option>
          <option value="AES">AES</option>
          <option value="OTP">OTP</option>
          <option value="3DES">3DES</option>
        </select>
      </div>
    </div>
  );
};

export default EncryptionApp;
