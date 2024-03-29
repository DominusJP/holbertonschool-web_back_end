import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((results) => {
      const status = results.map((result) => {
        if (result.status === 'rejected') {
          return {
            status: result.status,
            value: result.reason.toString(),
          };
        }
        return {
          status: result.status,
          value: result.value,
        };
      });
      return status;
    });
}
