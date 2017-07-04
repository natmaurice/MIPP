#ifndef CMPNEQTEST_HPP_
#define CMPNEQTEST_HPP_

#include <cppunit/extensions/HelperMacros.h>

class CmpneqTest : public CppUnit::TestFixture
{
	CPPUNIT_TEST_SUITE(CmpneqTest);

#if defined(MIPP_BW)
	CPPUNIT_TEST(test_reg_cmpneq_int8);
	CPPUNIT_TEST(test_Reg_cmpneq_int8);

	CPPUNIT_TEST(test_reg_cmpneq_int16);
	CPPUNIT_TEST(test_Reg_cmpneq_int16);
#endif

	CPPUNIT_TEST(test_reg_cmpneq_int32);
	CPPUNIT_TEST(test_Reg_cmpneq_int32);

	CPPUNIT_TEST(test_reg_cmpneq_float);
	CPPUNIT_TEST(test_Reg_cmpneq_float);

#if defined(MIPP_64BIT)
#if !defined(MIPP_SSE) || (defined(MIPP_SSE) && MIPP_INSTR_VERSION >= 41)
	CPPUNIT_TEST(test_reg_cmpneq_int64);
	CPPUNIT_TEST(test_Reg_cmpneq_int64);
#endif

	CPPUNIT_TEST(test_reg_cmpneq_double);
	CPPUNIT_TEST(test_Reg_cmpneq_double);
#endif

	CPPUNIT_TEST_SUITE_END();

public:
	void setUp();
	void tearDown();

	template <typename T>
	void test_reg_cmpneq();
	void test_reg_cmpneq_int8();
	void test_reg_cmpneq_int16();
	void test_reg_cmpneq_int32();
	void test_reg_cmpneq_int64();
	void test_reg_cmpneq_float();
	void test_reg_cmpneq_double();

	template <typename T>
	void test_Reg_cmpneq();
	void test_Reg_cmpneq_int8();
	void test_Reg_cmpneq_int16();
	void test_Reg_cmpneq_int32();
	void test_Reg_cmpneq_int64();
	void test_Reg_cmpneq_float();
	void test_Reg_cmpneq_double();
};

#endif  // CMPNEQTEST_HPP_
