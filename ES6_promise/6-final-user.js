import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const userData = await signUpUser(firstName, lastName);
  let photoData = null;

  try {
    photoData = await uploadPhoto(fileName);
  } catch (error) {
    photoData = `${error.name}: ${error.message}`;
  }

  const userPromiseResult = { status: 'fulfilled', value: userData };
  const photoPromiseResult = photoData.startsWith('Error') ? { status: 'rejected', value: photoData } : { status: 'fulfilled', value: photoData };

  return [userPromiseResult, photoPromiseResult];
}
