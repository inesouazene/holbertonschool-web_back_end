import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  // Appeler les fonctions signUpUser et uploadPhoto
  const signUpPromise = signUpUser(firstName, lastName);
  const uploadPromise = uploadPhoto(fileName);

  // Utiliser Promise.allSettled pour obtenir les résultats
  const results = await Promise.allSettled([signUpPromise, uploadPromise]);

  // Formater les résultats selon la spécification
  return results.map((result) => ({
    status: result.status,
    value: result.value || result.reason,
  }));
}
