# Generated from Nmod.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .NmodParser import NmodParser
else:
    from NmodParser import NmodParser

from Compiler import *
c = Compiler()


# This class defines a complete listener for a parse tree produced by NmodParser.
class NmodListener(ParseTreeListener):

    # Enter a parse tree produced by NmodParser#program.
    def enterProgram(self, ctx:NmodParser.ProgramContext):
        pass

    # Exit a parse tree produced by NmodParser#program.
    def exitProgram(self, ctx:NmodParser.ProgramContext):
        pass


    # Enter a parse tree produced by NmodParser#f_type.
    def enterF_type(self, ctx:NmodParser.F_typeContext):
        pass

    # Exit a parse tree produced by NmodParser#f_type.
    def exitF_type(self, ctx:NmodParser.F_typeContext):
        pass


    # Enter a parse tree produced by NmodParser#variables.
    def enterVariables(self, ctx:NmodParser.VariablesContext):
        pass

    # Exit a parse tree produced by NmodParser#variables.
    def exitVariables(self, ctx:NmodParser.VariablesContext):
        pass


    # Enter a parse tree produced by NmodParser#id_decl.
    def enterId_decl(self, ctx:NmodParser.Id_declContext):
        pass

    # Exit a parse tree produced by NmodParser#id_decl.
    def exitId_decl(self, ctx:NmodParser.Id_declContext):
        pass


    # Enter a parse tree produced by NmodParser#id_access.
    def enterId_access(self, ctx:NmodParser.Id_accessContext):
        pass

    # Exit a parse tree produced by NmodParser#id_access.
    def exitId_access(self, ctx:NmodParser.Id_accessContext):
        pass


    # Enter a parse tree produced by NmodParser#modules.
    def enterModules(self, ctx:NmodParser.ModulesContext):
        pass

    # Exit a parse tree produced by NmodParser#modules.
    def exitModules(self, ctx:NmodParser.ModulesContext):
        pass


    # Enter a parse tree produced by NmodParser#main.
    def enterMain(self, ctx:NmodParser.MainContext):
        pass

    # Exit a parse tree produced by NmodParser#main.
    def exitMain(self, ctx:NmodParser.MainContext):
        pass


    # Enter a parse tree produced by NmodParser#block.
    def enterBlock(self, ctx:NmodParser.BlockContext):
        pass

    # Exit a parse tree produced by NmodParser#block.
    def exitBlock(self, ctx:NmodParser.BlockContext):
        pass


    # Enter a parse tree produced by NmodParser#statute.
    def enterStatute(self, ctx:NmodParser.StatuteContext):
        pass

    # Exit a parse tree produced by NmodParser#statute.
    def exitStatute(self, ctx:NmodParser.StatuteContext):
        pass


    # Enter a parse tree produced by NmodParser#assignment.
    def enterAssignment(self, ctx:NmodParser.AssignmentContext):
        pass

    # Exit a parse tree produced by NmodParser#assignment.
    def exitAssignment(self, ctx:NmodParser.AssignmentContext):
        pass


    # Enter a parse tree produced by NmodParser#condition.
    def enterCondition(self, ctx:NmodParser.ConditionContext):
        pass

    # Exit a parse tree produced by NmodParser#condition.
    def exitCondition(self, ctx:NmodParser.ConditionContext):
        pass


    # Enter a parse tree produced by NmodParser#cicle.
    def enterCicle(self, ctx:NmodParser.CicleContext):
        pass

    # Exit a parse tree produced by NmodParser#cicle.
    def exitCicle(self, ctx:NmodParser.CicleContext):
        pass


    # Enter a parse tree produced by NmodParser#reading.
    def enterReading(self, ctx:NmodParser.ReadingContext):
        pass

    # Exit a parse tree produced by NmodParser#reading.
    def exitReading(self, ctx:NmodParser.ReadingContext):
        pass


    # Enter a parse tree produced by NmodParser#writing.
    def enterWriting(self, ctx:NmodParser.WritingContext):
        pass

    # Exit a parse tree produced by NmodParser#writing.
    def exitWriting(self, ctx:NmodParser.WritingContext):
        pass


    # Enter a parse tree produced by NmodParser#call_module.
    def enterCall_module(self, ctx:NmodParser.Call_moduleContext):
        pass

    # Exit a parse tree produced by NmodParser#call_module.
    def exitCall_module(self, ctx:NmodParser.Call_moduleContext):
        pass


    # Enter a parse tree produced by NmodParser#special_function.
    def enterSpecial_function(self, ctx:NmodParser.Special_functionContext):
        pass

    # Exit a parse tree produced by NmodParser#special_function.
    def exitSpecial_function(self, ctx:NmodParser.Special_functionContext):
        pass


    # Enter a parse tree produced by NmodParser#expression.
    def enterExpression(self, ctx:NmodParser.ExpressionContext):
        pass

    # Exit a parse tree produced by NmodParser#expression.
    def exitExpression(self, ctx:NmodParser.ExpressionContext):
        pass


    # Enter a parse tree produced by NmodParser#sub_exp.
    def enterSub_exp(self, ctx:NmodParser.Sub_expContext):
        pass

    # Exit a parse tree produced by NmodParser#sub_exp.
    def exitSub_exp(self, ctx:NmodParser.Sub_expContext):
        pass


    # Enter a parse tree produced by NmodParser#exp.
    def enterExp(self, ctx:NmodParser.ExpContext):
        pass

    # Exit a parse tree produced by NmodParser#exp.
    def exitExp(self, ctx:NmodParser.ExpContext):
        pass


    # Enter a parse tree produced by NmodParser#term.
    def enterTerm(self, ctx:NmodParser.TermContext):
        pass

    # Exit a parse tree produced by NmodParser#term.
    def exitTerm(self, ctx:NmodParser.TermContext):
        pass


    # Enter a parse tree produced by NmodParser#factor.
    def enterFactor(self, ctx:NmodParser.FactorContext):
        pass

    # Exit a parse tree produced by NmodParser#factor.
    def exitFactor(self, ctx:NmodParser.FactorContext):
        pass


    # Enter a parse tree produced by NmodParser#var_cte.
    def enterVar_cte(self, ctx:NmodParser.Var_cteContext):
        pass

    # Exit a parse tree produced by NmodParser#var_cte.
    def exitVar_cte(self, ctx:NmodParser.Var_cteContext):
        pass


    # Enter a parse tree produced by NmodParser#r_return.
    def enterR_return(self, ctx:NmodParser.R_returnContext):
        pass

    # Exit a parse tree produced by NmodParser#r_return.
    def exitR_return(self, ctx:NmodParser.R_returnContext):
        pass


    # Enter a parse tree produced by NmodParser#rnom.
    def enterRnom(self, ctx:NmodParser.RnomContext):
        pass

    # Exit a parse tree produced by NmodParser#rnom.
    def exitRnom(self, ctx:NmodParser.RnomContext):
        pass


    # Enter a parse tree produced by NmodParser#rexp.
    def enterRexp(self, ctx:NmodParser.RexpContext):
        pass

    # Exit a parse tree produced by NmodParser#rexp.
    def exitRexp(self, ctx:NmodParser.RexpContext):
        pass


    # Enter a parse tree produced by NmodParser#rgamma.
    def enterRgamma(self, ctx:NmodParser.RgammaContext):
        pass

    # Exit a parse tree produced by NmodParser#rgamma.
    def exitRgamma(self, ctx:NmodParser.RgammaContext):
        pass


    # Enter a parse tree produced by NmodParser#points.
    def enterPoints(self, ctx:NmodParser.PointsContext):
        pass

    # Exit a parse tree produced by NmodParser#points.
    def exitPoints(self, ctx:NmodParser.PointsContext):
        pass


    # Enter a parse tree produced by NmodParser#lines.
    def enterLines(self, ctx:NmodParser.LinesContext):
        pass

    # Exit a parse tree produced by NmodParser#lines.
    def exitLines(self, ctx:NmodParser.LinesContext):
        pass


    # Enter a parse tree produced by NmodParser#text.
    def enterText(self, ctx:NmodParser.TextContext):
        pass

    # Exit a parse tree produced by NmodParser#text.
    def exitText(self, ctx:NmodParser.TextContext):
        pass


    # Enter a parse tree produced by NmodParser#barplot.
    def enterBarplot(self, ctx:NmodParser.BarplotContext):
        pass

    # Exit a parse tree produced by NmodParser#barplot.
    def exitBarplot(self, ctx:NmodParser.BarplotContext):
        pass


    # Enter a parse tree produced by NmodParser#dotchart.
    def enterDotchart(self, ctx:NmodParser.DotchartContext):
        pass

    # Exit a parse tree produced by NmodParser#dotchart.
    def exitDotchart(self, ctx:NmodParser.DotchartContext):
        pass


    # Enter a parse tree produced by NmodParser#piechart.
    def enterPiechart(self, ctx:NmodParser.PiechartContext):
        pass

    # Exit a parse tree produced by NmodParser#piechart.
    def exitPiechart(self, ctx:NmodParser.PiechartContext):
        pass


    # Enter a parse tree produced by NmodParser#xyplot.
    def enterXyplot(self, ctx:NmodParser.XyplotContext):
        pass

    # Exit a parse tree produced by NmodParser#xyplot.
    def exitXyplot(self, ctx:NmodParser.XyplotContext):
        pass


    # Enter a parse tree produced by NmodParser#densityplot.
    def enterDensityplot(self, ctx:NmodParser.DensityplotContext):
        pass

    # Exit a parse tree produced by NmodParser#densityplot.
    def exitDensityplot(self, ctx:NmodParser.DensityplotContext):
        pass


    # Enter a parse tree produced by NmodParser#histogram.
    def enterHistogram(self, ctx:NmodParser.HistogramContext):
        pass

    # Exit a parse tree produced by NmodParser#histogram.
    def exitHistogram(self, ctx:NmodParser.HistogramContext):
        pass


    # Enter a parse tree produced by NmodParser#sin.
    def enterSin(self, ctx:NmodParser.SinContext):
        pass

    # Exit a parse tree produced by NmodParser#sin.
    def exitSin(self, ctx:NmodParser.SinContext):
        pass


    # Enter a parse tree produced by NmodParser#cos.
    def enterCos(self, ctx:NmodParser.CosContext):
        pass

    # Exit a parse tree produced by NmodParser#cos.
    def exitCos(self, ctx:NmodParser.CosContext):
        pass


    # Enter a parse tree produced by NmodParser#tan.
    def enterTan(self, ctx:NmodParser.TanContext):
        pass

    # Exit a parse tree produced by NmodParser#tan.
    def exitTan(self, ctx:NmodParser.TanContext):
        pass


    # Enter a parse tree produced by NmodParser#asin.
    def enterAsin(self, ctx:NmodParser.AsinContext):
        pass

    # Exit a parse tree produced by NmodParser#asin.
    def exitAsin(self, ctx:NmodParser.AsinContext):
        pass


    # Enter a parse tree produced by NmodParser#acos.
    def enterAcos(self, ctx:NmodParser.AcosContext):
        pass

    # Exit a parse tree produced by NmodParser#acos.
    def exitAcos(self, ctx:NmodParser.AcosContext):
        pass


    # Enter a parse tree produced by NmodParser#atan.
    def enterAtan(self, ctx:NmodParser.AtanContext):
        pass

    # Exit a parse tree produced by NmodParser#atan.
    def exitAtan(self, ctx:NmodParser.AtanContext):
        pass


    # Enter a parse tree produced by NmodParser#atan2.
    def enterAtan2(self, ctx:NmodParser.Atan2Context):
        pass

    # Exit a parse tree produced by NmodParser#atan2.
    def exitAtan2(self, ctx:NmodParser.Atan2Context):
        pass


    # Enter a parse tree produced by NmodParser#log.
    def enterLog(self, ctx:NmodParser.LogContext):
        pass

    # Exit a parse tree produced by NmodParser#log.
    def exitLog(self, ctx:NmodParser.LogContext):
        pass


    # Enter a parse tree produced by NmodParser#log10.
    def enterLog10(self, ctx:NmodParser.Log10Context):
        pass

    # Exit a parse tree produced by NmodParser#log10.
    def exitLog10(self, ctx:NmodParser.Log10Context):
        pass


    # Enter a parse tree produced by NmodParser#exponent.
    def enterExponent(self, ctx:NmodParser.ExponentContext):
        pass

    # Exit a parse tree produced by NmodParser#exponent.
    def exitExponent(self, ctx:NmodParser.ExponentContext):
        pass


    # Enter a parse tree produced by NmodParser#f_max.
    def enterF_max(self, ctx:NmodParser.F_maxContext):
        pass

    # Exit a parse tree produced by NmodParser#f_max.
    def exitF_max(self, ctx:NmodParser.F_maxContext):
        pass


    # Enter a parse tree produced by NmodParser#f_min.
    def enterF_min(self, ctx:NmodParser.F_minContext):
        pass

    # Exit a parse tree produced by NmodParser#f_min.
    def exitF_min(self, ctx:NmodParser.F_minContext):
        pass


    # Enter a parse tree produced by NmodParser#f_range.
    def enterF_range(self, ctx:NmodParser.F_rangeContext):
        pass

    # Exit a parse tree produced by NmodParser#f_range.
    def exitF_range(self, ctx:NmodParser.F_rangeContext):
        pass


    # Enter a parse tree produced by NmodParser#f_sum.
    def enterF_sum(self, ctx:NmodParser.F_sumContext):
        pass

    # Exit a parse tree produced by NmodParser#f_sum.
    def exitF_sum(self, ctx:NmodParser.F_sumContext):
        pass


    # Enter a parse tree produced by NmodParser#diff.
    def enterDiff(self, ctx:NmodParser.DiffContext):
        pass

    # Exit a parse tree produced by NmodParser#diff.
    def exitDiff(self, ctx:NmodParser.DiffContext):
        pass


    # Enter a parse tree produced by NmodParser#prod.
    def enterProd(self, ctx:NmodParser.ProdContext):
        pass

    # Exit a parse tree produced by NmodParser#prod.
    def exitProd(self, ctx:NmodParser.ProdContext):
        pass


    # Enter a parse tree produced by NmodParser#mean.
    def enterMean(self, ctx:NmodParser.MeanContext):
        pass

    # Exit a parse tree produced by NmodParser#mean.
    def exitMean(self, ctx:NmodParser.MeanContext):
        pass


    # Enter a parse tree produced by NmodParser#median.
    def enterMedian(self, ctx:NmodParser.MedianContext):
        pass

    # Exit a parse tree produced by NmodParser#median.
    def exitMedian(self, ctx:NmodParser.MedianContext):
        pass


    # Enter a parse tree produced by NmodParser#quantile.
    def enterQuantile(self, ctx:NmodParser.QuantileContext):
        pass

    # Exit a parse tree produced by NmodParser#quantile.
    def exitQuantile(self, ctx:NmodParser.QuantileContext):
        pass


    # Enter a parse tree produced by NmodParser#rank.
    def enterRank(self, ctx:NmodParser.RankContext):
        pass

    # Exit a parse tree produced by NmodParser#rank.
    def exitRank(self, ctx:NmodParser.RankContext):
        pass


    # Enter a parse tree produced by NmodParser#var.
    def enterVar(self, ctx:NmodParser.VarContext):
        pass

    # Exit a parse tree produced by NmodParser#var.
    def exitVar(self, ctx:NmodParser.VarContext):
        pass


    # Enter a parse tree produced by NmodParser#sd.
    def enterSd(self, ctx:NmodParser.SdContext):
        pass

    # Exit a parse tree produced by NmodParser#sd.
    def exitSd(self, ctx:NmodParser.SdContext):
        pass


    # Enter a parse tree produced by NmodParser#cor.
    def enterCor(self, ctx:NmodParser.CorContext):
        pass

    # Exit a parse tree produced by NmodParser#cor.
    def exitCor(self, ctx:NmodParser.CorContext):
        pass


    # Enter a parse tree produced by NmodParser#cov.
    def enterCov(self, ctx:NmodParser.CovContext):
        pass

    # Exit a parse tree produced by NmodParser#cov.
    def exitCov(self, ctx:NmodParser.CovContext):
        pass


    # Enter a parse tree produced by NmodParser#f_round.
    def enterF_round(self, ctx:NmodParser.F_roundContext):
        pass

    # Exit a parse tree produced by NmodParser#f_round.
    def exitF_round(self, ctx:NmodParser.F_roundContext):
        pass


    # Enter a parse tree produced by NmodParser#transpose.
    def enterTranspose(self, ctx:NmodParser.TransposeContext):
        pass

    # Exit a parse tree produced by NmodParser#transpose.
    def exitTranspose(self, ctx:NmodParser.TransposeContext):
        pass


    # Enter a parse tree produced by NmodParser#diagonal.
    def enterDiagonal(self, ctx:NmodParser.DiagonalContext):
        pass

    # Exit a parse tree produced by NmodParser#diagonal.
    def exitDiagonal(self, ctx:NmodParser.DiagonalContext):
        pass


    # Enter a parse tree produced by NmodParser#ginv.
    def enterGinv(self, ctx:NmodParser.GinvContext):
        pass

    # Exit a parse tree produced by NmodParser#ginv.
    def exitGinv(self, ctx:NmodParser.GinvContext):
        pass


    # Enter a parse tree produced by NmodParser#rowsum.
    def enterRowsum(self, ctx:NmodParser.RowsumContext):
        pass

    # Exit a parse tree produced by NmodParser#rowsum.
    def exitRowsum(self, ctx:NmodParser.RowsumContext):
        pass


    # Enter a parse tree produced by NmodParser#colsum.
    def enterColsum(self, ctx:NmodParser.ColsumContext):
        pass

    # Exit a parse tree produced by NmodParser#colsum.
    def exitColsum(self, ctx:NmodParser.ColsumContext):
        pass


    # Enter a parse tree produced by NmodParser#load.
    def enterLoad(self, ctx:NmodParser.LoadContext):
        pass

    # Exit a parse tree produced by NmodParser#load.
    def exitLoad(self, ctx:NmodParser.LoadContext):
        pass


    # Enter a parse tree produced by NmodParser#data.
    def enterData(self, ctx:NmodParser.DataContext):
        pass

    # Exit a parse tree produced by NmodParser#data.
    def exitData(self, ctx:NmodParser.DataContext):
        pass


    # Enter a parse tree produced by NmodParser#library.
    def enterLibrary(self, ctx:NmodParser.LibraryContext):
        pass

    # Exit a parse tree produced by NmodParser#library.
    def exitLibrary(self, ctx:NmodParser.LibraryContext):
        pass


    # Enter a parse tree produced by NmodParser#rpois.
    def enterRpois(self, ctx:NmodParser.RpoisContext):
        pass

    # Exit a parse tree produced by NmodParser#rpois.
    def exitRpois(self, ctx:NmodParser.RpoisContext):
        pass


    # Enter a parse tree produced by NmodParser#rweibull.
    def enterRweibull(self, ctx:NmodParser.RweibullContext):
        pass

    # Exit a parse tree produced by NmodParser#rweibull.
    def exitRweibull(self, ctx:NmodParser.RweibullContext):
        pass


    # Enter a parse tree produced by NmodParser#rbinom.
    def enterRbinom(self, ctx:NmodParser.RbinomContext):
        pass

    # Exit a parse tree produced by NmodParser#rbinom.
    def exitRbinom(self, ctx:NmodParser.RbinomContext):
        pass


    # Enter a parse tree produced by NmodParser#rgeom.
    def enterRgeom(self, ctx:NmodParser.RgeomContext):
        pass

    # Exit a parse tree produced by NmodParser#rgeom.
    def exitRgeom(self, ctx:NmodParser.RgeomContext):
        pass


    # Enter a parse tree produced by NmodParser#runif.
    def enterRunif(self, ctx:NmodParser.RunifContext):
        pass

    # Exit a parse tree produced by NmodParser#runif.
    def exitRunif(self, ctx:NmodParser.RunifContext):
        pass


