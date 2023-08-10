import axios from "axios";

const put = async ({ path = "/", data, token }) => {
  try {
    const url = `${import.meta.env.VITE_API_ENDPOINT}${path}`;

    await axios
      .put(url, data, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      })
      .then((response) => {
        const json = response.json();
        if (!response.ok) {
          throw new Error(json.message);
        }
        return json;
      });
  } catch (error) {
    return error.response;
  }
};

export default put;
