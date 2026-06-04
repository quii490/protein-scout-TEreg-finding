---
type: protein-evaluation
gene: "DIMT1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DIMT1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DIMT1 / DIMT1L |
| 蛋白名称 | Dimethyladenosine transferase |
| 蛋白大小 | 313 aa / 35.2 kDa |
| UniProt ID | Q9UNQ2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Cytosol; UniProt: Nucleus, nucleoplasm; Nucleus, nucleolus |
| 蛋白大小 | 10/10 | x1 | 10 | 313 aa / 35.2 kDa |
| 研究新颖性 | 10/10 | x5 | 50 | PubMed strict=13 篇 (<=20->10) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=92.0; PDB: 1ZQ9, 6W6C, 6W6F, 7MQA, 7WTS |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR001737, IPR020596, IPR020598, IPR011530, IPR029 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **142.5/180** | |
| **归一化总分** | | | **79.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Nucleus, nucleoplasm; Nucleus, nucleolus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cytosol (GO:0005829)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)
- small-subunit processome (GO:0032040)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 13 |
| PubMed broad count | 22 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DIMT1L |

**关键文献**:
1. Human DIMT1 generates N(2)(6,6)A-dimethylation-containing small RNAs.. *The Journal of biological chemistry*. PMID: 34473991
2. Structural and functional characterization of archaeal DIMT1 unveils distinct protein dynamics essential for efficient catalysis.. *Structure (London, England : 1993)*. PMID: 39146930
3. Identification of a longevity gene through evolutionary rate covariation of insect mito-nuclear genomes.. *Nature aging*. PMID: 38834883
4. Structural and catalytic roles of the human 18S rRNA methyltransferases DIMT1 in ribosome assembly and translation.. *The Journal of biological chemistry*. PMID: 32616653
5. Ribosomal biogenesis regulator DIMT1 controls β-cell protein synthesis, mitochondrial function, and insulin secretion.. *The Journal of biological chemistry*. PMID: 35148993

**评价**: 极度新颖，几乎未被系统研究（PubMed <=20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.0 |
| 高置信度残基 (pLDDT>90) 占比 | 87.9% |
| 置信残基 (pLDDT 70-90) 占比 | 3.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.6% |
| 低置信 (pLDDT<50) 占比 | 7.0% |
| 有序区域 (pLDDT>70) 占比 | 91.4% |
| 可用 PDB 条目 | 1ZQ9, 6W6C, 6W6F, 7MQA, 7WTS |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1ZQ9, 6W6C, 6W6F, 7MQA, 7WTS）+ AlphaFold极高置信度预测（pLDDT=92.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR001737, IPR020596, IPR020598, IPR011530, IPR029063; Pfam: PF00398 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MED29 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| MAGED1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HDGF | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21907836|imex:IM-17230 |
| VCAM1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-17358|pubmed:22623428 |
| EBI-6249674 | psi-mi:"MI:0096"(pull down) | pubmed:22623228|imex:IM-17422 |
| MYC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:17314511 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| CAND1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| FBL | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| RPS6 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.0 + PDB: 1ZQ9, 6W6C, 6W6F, 7MQA, 7WTS | pLDDT=92.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleoplasm; Nucleus, nucleolus / Nucleoli, Nucleoli rim; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ****

**核心优势**:
1. DIMT1 -- Dimethyladenosine transferase，极度新颖，几乎未被系统研究（PubMed <=20篇）。
2. 蛋白大小313 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 13 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UNQ2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000086189-DIMT1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DIMT1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UNQ2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
