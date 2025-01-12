import { ContactInfo } from "../types/ContactInfo";
import axios, { AxiosInstance, AxiosRequestConfig } from "axios";

    export function postContactInfo(input: ContactInfo): void {
        
        const httpClient: AxiosInstance = axios.create();
        const axiosConfig: AxiosRequestConfig = {
            url: '/ContactUs',
            method: 'post',
            baseURL: 'http://127.0.0.1:8000',
            headers: {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': 'http://localhost:3000/'},
            data: input
        }
        try {
            httpClient.request(axiosConfig);
        }
        catch(error: unknown) {
            console.log('and error happend')
            console.error(error)
            throw error
        }       
    }