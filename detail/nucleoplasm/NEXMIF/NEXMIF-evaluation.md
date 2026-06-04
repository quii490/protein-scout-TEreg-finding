---
type: protein-evaluation
gene: "NEXMIF"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, recovery, re-evaluation]
status: scored
---

## NEXMIF 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NEXMIF / KIAA2022 |
| 蛋白名称 | Neurite extension and migration factor |
| 蛋白大小 | 1516 aa / 167.6 kDa |
| UniProt ID | Q5QGS0 |
| 数据采集时间 | 2026-06-03 23:37:00 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm; 额外: Midbody, Cytosol; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 5/10 | x1 | 5 | 1516 aa / 167.6 kDa |
| 研究新颖性 | 8/10 | x5 | 40 | PubMed strict=37 篇 (21-40 -> 8) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=40.6; PDB: 无 |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR032757, IPR042794; Pfam: PF15735 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | -- | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Midbody, Cytosol | Supported |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

**GO Cellular Component**:
- cytosol (GO:0005829)
- midbody (GO:0030496)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 蛋白偏小/偏大，实验操作有一定难度。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 37 |
| PubMed broad count | 60 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA2022 |

**关键文献**:
1. NEXMIF encephalopathy: an X-linked disorder with male and female phenotypic patterns.. *Genetics in medicine : official journal of the American College of Medical Genetics*. PMID: 33144681
2. Dissecting genetics of spectrum of epilepsies with eyelid myoclonia by exome sequencing.. *Epilepsia*. PMID: 38088023
3. Infantile spasms caused by NEXMIF mutation: A case report and literature review.. *Applied neuropsychology. Child*. PMID: 37313861
4. Torpedo Maculopathy Associated with NEXMIF Mutation.. *Molecular syndromology*. PMID: 31602197
5. KIAA2022/NEXMIF c.1882C>T (p.Arg628*) Variant in a Romanian Patient with Neurodevelopmental Disorders and Epilepsy: A Case Report and Systematic Review.. *Life (Basel, Switzerland)*. PMID: 40141841

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 40.6 |
| 高置信度残基 (pLDDT>90) 占比 | 0.1% |
| 置信残基 (pLDDT 70-90) 占比 | 3.8% |
| 中等置信 (pLDDT 50-70) 占比 | 10.6% |
| 低置信 (pLDDT<50) 占比 | 85.5% |
| 有序区域 (pLDDT>70) 占比 | 3.9% |
| 可用 PDB 条目 | 无 |

**PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。**

**评价**: AlphaFold 预测质量有限（pLDDT=40.6），有序残基占 3.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR032757, IPR042794; Pfam: PF15735 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=40.6 + PDB: 无 | pLDDT=40.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm; 额外: Midbody, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ 

**核心优势**:
1. NEXMIF -- Neurite extension and migration factor，非常新颖，仅有少数基础研究。
2. 蛋白大小1516 aa，蛋白偏小/偏大，实验操作有一定难度。

**风险/不确定性**:
1. PubMed 37 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=40.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q5QGS0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000050030-NEXMIF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NEXMIF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q5QGS0
- STRING: https://string-db.org/network/9606.NEXMIF
- Packet data timestamp: 2026-06-03 23:37:00

---
*本报告为全量重评估 (Full Re-evaluation) -- Recovery from false-rejection。所有评分基于最新harvest packet数据，使用标准/180评分体系计算。*
