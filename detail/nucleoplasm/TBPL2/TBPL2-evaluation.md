---
type: protein-evaluation
gene: "TBPL2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TBPL2 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TBPL2 / TBP2, TRF3 |
| 蛋白名称 | TATA box-binding protein-like 2 |
| 蛋白大小 | 343 aa / 38.0 kDa |
| UniProt ID | Q6SJ96 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 343 aa / 38.0 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=17 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=69.4; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000814, IPR030491, IPR012295, IPR033710; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 3 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **130.0/180** | |
| **归一化总分** | | | **72.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- female germ cell nucleus (GO:0001674)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 17 |
| PubMed broad count | 41 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TBP2, TRF3 |

**关键文献**:
1. What defines the maternal transcriptome?. *Biochemical Society transactions*. PMID: 34415300
2. Participation of the TBP-associated factors (TAFs) in cell differentiation.. *Journal of cellular physiology*. PMID: 38126142
3. Genetic variants in diminished ovarian reserve and premature ovarian insufficiency: implications for assisted reproductive outcomes.. *Journal of assisted reproduction and genetics*. PMID: 40936058
4. Evaluation of an Updated Gene Panel as a Diagnostic Tool for Both Male and Female Infertility.. *Reproductive sciences (Thousand Oaks, Calif.)*. PMID: 38664359
5. Functional implications of paralog genes in polyglutamine spinocerebellar ataxias.. *Human genetics*. PMID: 37845370

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 69.4 |
| 高置信度残基 (pLDDT>90) 占比 | 51.0% |
| 置信残基 (pLDDT 70-90) 占比 | 1.2% |
| 中等置信 (pLDDT 50-70) 占比 | 4.7% |
| 低置信 (pLDDT<50) 占比 | 43.1% |
| 有序区域 (pLDDT>70) 占比 | 52.2% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=69.4），有序残基占 52.2%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000814, IPR030491, IPR012295, IPR033710; Pfam: PF00352 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GTF2B | 0.994 | 0.834 | — |
| TAF3 | 0.993 | 0.328 | — |
| TBPL1 | 0.938 | 0.277 | — |
| TAF6 | 0.936 | 0.831 | — |
| MYOD1 | 0.931 | 0.071 | — |
| BTAF1 | 0.929 | 0.842 | — |
| TAF8 | 0.919 | 0.838 | — |
| TAF10 | 0.919 | 0.831 | — |
| TAF12 | 0.918 | 0.831 | — |
| NFYA | 0.918 | 0.104 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Taf3 | psi-mi:"MI:0071"(molecular sieving) | pubmed:17704303|imex:IM-19784 |
| EBI-1571481 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:17704303|imex:IM-19784 |
| AFG2A | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:38554706|imex:IM-30175 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 3
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 3 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=69.4 + PDB: 无 | pLDDT=69.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 3 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. TBPL2 — TATA box-binding protein-like 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小343 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 17 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=69.4），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6SJ96
- Protein Atlas: https://www.proteinatlas.org/ENSG00000182521-TBPL2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TBPL2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6SJ96
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6SJ96-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
