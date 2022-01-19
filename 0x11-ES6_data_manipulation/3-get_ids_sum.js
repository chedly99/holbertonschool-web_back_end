export default function getStudentIdsSum(students) {
  return students.reduce((sum, { id }) => sum + id, 0);
}
