import React,{createContext,useState} from "react";
interface EncryptionProviderProps {
    children: React.ReactNode;
}
interface EncryptTextParams {
    text: string;
}

interface EncryptionContextType {
    encryptionText: string;
  encryptionKey: string;
  decryptionKey: string;
  encryptionMethod: string;
  decryptionText:string;
  setDecryptionText:(key:string) =>void;
  setEncryptionKey: (key: string) => void;
  setDecryptionKey: (key: string) => void;
  setEncryptionText:(key: string) => void;
  setEncryptionAlgorithm: (method: string) => void;
  encryptText: ({ text }: EncryptTextParams) => Promise<void>;
  decryptText: ({ text }: EncryptTextParams) => Promise<void>;
  error :string;
}

const defaultValues: EncryptionContextType = {
    encryptionText: "",
    encryptionKey: "",
    decryptionKey: "",
    encryptionMethod: "",
    setEncryptionKey: () => {},
    setDecryptionKey: () => {},
    setDecryptionText:() => {},
    setEncryptionAlgorithm: () => {},
    encryptText: async () => {},
    decryptText: async () => {},
    setEncryptionText:() => {},
    decryptionText:"",
    error :""
    
  };

export const EncryptionContext = createContext<EncryptionContextType >(defaultValues);

export const EncryptionProvider = ({ children }: EncryptionProviderProps) =>{
    const [encryptionText,setEncryptionText] = useState<string>("");
    const [decryptionText,setDecryptionText] = useState<string>("");
    const [encryptionKey,setEncryptionKey] = useState<string>("");
    const [decryptionKey,setDecryptionKey] = useState<string>("");
    const [encryptionMethod,setEncryptionAlgorithm] = useState<string>("");
    // const [error,setError] = useState<string>("");  
    

    const encryptText = async ({ text }: EncryptTextParams): Promise<void> => {
        try {
            const response = await fetch("https://localhost:8443/encrypt/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    message:text,
                    key: encryptionKey,
                    algorithm:encryptionMethod,
                }),
            });
            if (!response.ok) {
                const errorData = await response.json(); // Try to extract error details from the server
                throw new Error(
                  `Encryption failed! Status: ${response.status} - ${errorData?.message || "Unknown error"}`
                );
              }
            // Handle response if needed
            const data = await response.json();
            
            setEncryptionText(data.encrypted_message);
        } catch (error) {
            console.error("Encryption failed", error);
        }
    };

    // decrypt text
    const decryptText = async({text}:EncryptTextParams): Promise<void> =>{
        try{
            const response = await fetch("https://localhost:8443/decrypt/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    encrypted_message:text,
                    key: decryptionKey,
                    algorithm:encryptionMethod,
                }),
            });
            const data = await response.json()
            if (response.ok){
                setDecryptionText(data.decrypted_message);
                // setError("")
            }
                
            
            

        } catch(err){
            console.error("Decryption faild" , err);
            setDecryptionText("");
            // setError("Faild to decrypt message");
        }
    };

    return (
        <EncryptionContext.Provider
            value={{
                error :"",
                encryptionText,
                setEncryptionText,
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
            }}
        >
            {children}
        </EncryptionContext.Provider>
    )};
