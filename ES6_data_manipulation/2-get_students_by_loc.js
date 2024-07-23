export default function getListStudentgetStudentsByLocationIds(students, city) {
  return students.filter((student) => student.location === city);
}
