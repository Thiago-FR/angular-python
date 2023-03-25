import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { Observable } from 'rxjs';
import { IUser } from '../interface/User';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class UserService {
  private baseApiUrl = environment.baseURL;
  private apiUrl = `${this.baseApiUrl}/user`

  constructor(private http: HttpClient) { }

  getAllUsers(): Observable<IUser[]> {
    return this.http.get<IUser[]>(this.apiUrl)
  }

  createUser(user: IUser) {
    return this.http.post<any>(this.apiUrl, user)
  }

  putUser(user: IUser) {
    return this.http.put<IUser>(`${this.apiUrl}/${user._id}`, user)
  }

  deleteUser(id: string) {
    return this.http.delete<IUser>(`${this.apiUrl}/${id}`)
  }
}
