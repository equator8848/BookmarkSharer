import axios from 'axios'

const instance = axios.create({
  // http://127.0.0.1:8000/bookmarkSharer/api/ https://www.equator8848.xyz/bookmarkSharer/api/
  baseURL: 'https://www.equator8848.xyz/bookmarkSharer/api/'
})

export default {
  request: instance,
  statusCode: {
    FAIL: -1,
    SUCCESS: 2000,
    BAD_REQUEST: 4000,
    PARAMETER_ERROR: 4001,
    FORBIDDEN: 4003,
    SERVER_ERROR: 5000
  }
}
