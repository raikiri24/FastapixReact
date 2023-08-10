import axios from 'axios';

const get = async (path = '/', submittedPayload = {}, token = null, id = null) => {
  let data = {};
  try {
    let url = `${import.meta.env.VITE_API_ENDPOINT}${path}`;
    const params = {
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': "*" ,'Access-Control-Allow-Credentials': 'true'}
    };

    if (token !== null) {
      params.headers = {
        ...params.headers,
        Authorization: `Bearer ${token}`
      };
    }

    if (id !== null) {
      params.headers = {
        ...params.headers,
        'x-user-id': id
      };
    }

    const { as_is = false, ...payload } = submittedPayload;

    if (Object.keys(payload).length > 0) {
      let connector = '?';
      if (url.includes('?')) {
        connector = '&';
      }
      Object.keys(payload).forEach((item) => {
        if (as_is) {
          url = `${url}${connector}${item}=${encodeURIComponent(payload[item])}`;
        } else {
          url = `${url}${connector}${item}=${encodeURIComponent(JSON.stringify(payload[item]))}`;
        }
        connector = '&';
      });
    }

    const response = await axios.get(url, params);
    if ([200].includes(response.status)) {
      data = response.data;
    }
    return data;
  } catch (error) {
    return error.response;
  }
};

export default get;
