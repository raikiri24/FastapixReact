import axios from 'axios';
const headers = {
  'Access-Control-Allow-Origin': '*',
  'Content-Type': 'application/json'
};
const post = async (path = '/', data = {}) => {
  try {
    const url = `${import.meta.env.VITE_API_ENDPOINT}${path}`;
    let ret = {};
    ret = await axios.post(url, { ...data }, headers);
    return ret;
  } catch (error) {
    return error.response;
  }
};

export default post;
