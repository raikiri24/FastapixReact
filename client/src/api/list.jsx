import axios from "axios";

const list = async ({
  path = "/",
  limit = 12,
  page = 1,
  token,
  filters = {},
}) => {
  let data = {};
  try {
    let url = `${
      import.meta.env.VITE_API_ENDPOINT
    }${path}?limit=${limit}&page=${page}`;

    if (Object.keys(filters).length > 0) {
      Object.keys(filters).forEach((filter) => {
        url = `${url}&${filter}=${filters[filter]}`;
      });
    }

    const params = { headers: {} };

    if (token !== null) {
      params.headers = {
        ...params.headers,
        Authorization: `Bearer ${token}`,
      };
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

export default list;
