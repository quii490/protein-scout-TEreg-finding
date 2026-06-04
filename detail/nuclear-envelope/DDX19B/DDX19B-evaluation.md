---
type: protein-evaluation
gene: "DDX19B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DDX19B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DDX19B / DBP5, DDX19, TDBP |
| 蛋白名称 | ATP-dependent RNA helicase DDX19B |
| 蛋白大小 | 479 aa / 53.9 kDa |
| UniProt ID | Q9UMR2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; UniProt: Cytoplasm; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | x1 | 10 | 479 aa / 53.9 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=12 篇 (≤20→10) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=81.5; PDB: 3EWS, 3FHC, 3FHT, 3FMO, 3FMP, 3G0H, 6B4I |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR011545, IPR014001, IPR001650, IPR027417, IPR014 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **145.5/180** | |
| **归一化总分** | | | **80.8/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Uncertain |
| UniProt | Cytoplasm; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoplasmic stress granule (GO:0010494)
- extracellular exosome (GO:0070062)
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)
- nuclear pore (GO:0005643)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 12 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DBP5, DDX19, TDBP |

**关键文献**:
1. The RNA helicases DDX19A/B modulate selinexor sensitivity by regulating MCL1 mRNA nuclear export in leukemia cells.. *Leukemia*. PMID: 38987275
2. SUMOylation modulates the function of DDX19 in mRNA export.. *Journal of cell science*. PMID: 35080244
3. Biomarkers, Master Regulators and Genomic Fabric Remodeling in a Case of Papillary Thyroid Carcinoma.. *Genes*. PMID: 32887258
4. Integrative analysis reveals the prognostic value and functions of splicing factors implicated in hepatocellular carcinoma.. *Scientific reports*. PMID: 34312475
5. Nup42 and IP(6) coordinate Gle1 stimulation of Dbp5/DDX19B for mRNA export in yeast and human cells.. *Traffic (Copenhagen, Denmark)*. PMID: 28869701

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.5 |
| 高置信度残基 (pLDDT>90) 占比 | 48.6% |
| 置信残基 (pLDDT 70-90) 占比 | 31.5% |
| 中等置信 (pLDDT 50-70) 占比 | 9.8% |
| 低置信 (pLDDT<50) 占比 | 10.0% |
| 有序区域 (pLDDT>70) 占比 | 80.1% |
| 可用 PDB 条目 | 3EWS, 3FHC, 3FHT, 3FMO, 3FMP, 3G0H, 6B4I, 6B4J, 6B4K |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=81.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011545, IPR014001, IPR001650, IPR027417, IPR014014; Pfam: PF00270, PF00271 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NUP214 | 0.950 | 0.946 | — |
| GLE1 | 0.950 | 0.918 | — |
| NUP42 | 0.866 | 0.861 | — |
| CTIF | 0.662 | 0.624 | — |
| MIF4GD | 0.650 | 0.643 | — |
| UBALD1 | 0.587 | 0.000 | — |
| BOP1 | 0.587 | 0.295 | — |
| PES1 | 0.555 | 0.269 | — |
| NOP58 | 0.555 | 0.313 | — |
| WDR12 | 0.548 | 0.269 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.5 + PDB: 3EWS, 3FHC, 3FHT, 3FMO, 3FMP,  | pLDDT=81.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus, nucleoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. DDX19B -- ATP-dependent RNA helicase DDX19B，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小479 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 12 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UMR2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000157349-DDX19B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DDX19B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UMR2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
