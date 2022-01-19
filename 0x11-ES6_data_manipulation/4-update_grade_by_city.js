export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((s) => s.location === city)
    .map((s) => {
      const grades = newGrades.find((g) => g.studentId === s.id);
      const grade = grades ? grades.grade : 'N/A';
      return { ...s, grade };
    });
}
