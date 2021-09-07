const env = process.env.VUE_APP_ENV;

let envApiUrl = '';

if (env === 'production') {
  envApiUrl = 'https://startuptogether.pyhub.me';
} else if (env === 'staging') {
  envApiUrl = 'https://staging.startuptogether.pyhub.me';
} else {
  envApiUrl = `http://localhost`;
}

export const apiUrl = envApiUrl;
export const appName = 'startup-together';
