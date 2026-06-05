---
type: protein-evaluation
gene: "SRY"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SRY — REJECTED (研究热度过高 (PubMed strict=4227，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SRY / TDF |
| 蛋白名称 | Sex-determining region Y protein |
| 蛋白大小 | 204 aa / 23.9 kDa |
| UniProt ID | Q05066 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus speckle; Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 204 aa / 23.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=4227 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.6; PDB: 1HRY, 1HRZ, 1J46, 1J47, 2GZK, 6EDB, 7YHO |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR009071, IPR036910, IPR017253, IPR050140; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus speckle; Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4227 |
| PubMed broad count | 5915 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TDF |

**关键文献**:
1. Sex determination.. *Human molecular genetics*. PMID: 7849739
2. The SRY gene.. *Trends in endocrinology and metabolism: TEM*. PMID: 18407180
3. Sex-determining region Y gene promotes liver fibrosis and accounts for sexual dimorphism in its pathophysiology.. *Journal of hepatology*. PMID: 38336346
4. Whatever happened to SRY?. *Cellular and molecular life sciences : CMLS*. PMID: 11212323
5. SRY mediates male-specific susceptibility to acute liver injury.. *Cell communication and signaling : CCS*. PMID: 41331455

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.6 |
| 高置信度残基 (pLDDT>90) 占比 | 37.3% |
| 置信残基 (pLDDT 70-90) 占比 | 3.4% |
| 中等置信 (pLDDT 50-70) 占比 | 23.5% |
| 低置信 (pLDDT<50) 占比 | 35.8% |
| 有序区域 (pLDDT>70) 占比 | 40.7% |
| 可用 PDB 条目 | 1HRY, 1HRZ, 1J46, 1J47, 2GZK, 6EDB, 7YHO, 7YHP, 7YHQ, 9BVD |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.6），有序残基占 40.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR009071, IPR036910, IPR017253, IPR050140; Pfam: PF00505 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ZFY | 0.989 | 0.095 | — |
| NR5A1 | 0.986 | 0.098 | — |
| DMRT1 | 0.955 | 0.065 | — |
| UTY | 0.943 | 0.059 | — |
| WT1 | 0.938 | 0.095 | — |
| USP9Y | 0.907 | 0.000 | — |
| NR0B1 | 0.889 | 0.071 | — |
| ZFX | 0.868 | 0.095 | — |
| TSPY1 | 0.864 | 0.000 | — |
| AMH | 0.855 | 0.045 | — |

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
| 三维结构 | AlphaFold pLDDT=67.6 + PDB: 1HRY, 1HRZ, 1J46, 1J47, 2GZK,  | pLDDT=67.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus speckle; Cytoplasm; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SRY — Sex-determining region Y protein，研究基础较多，新颖性有限。
2. 蛋白大小204 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4227 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 4227 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q05066
- Protein Atlas: https://www.proteinatlas.org/ENSG00000184895-SRY/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SRY
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q05066
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q05066-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
