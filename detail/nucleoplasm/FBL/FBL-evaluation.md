---
type: protein-evaluation
gene: "FBL"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FBL — REJECTED (研究热度过高 (PubMed strict=186，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBL / FIB1, FLRN |
| 蛋白名称 | rRNA 2'-O-methyltransferase fibrillarin |
| 蛋白大小 | 321 aa / 33.8 kDa |
| UniProt ID | P22087 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoli fibrillar center; 额外: Nucleoplasm; UniProt: Nucleus, nucleolus; Nucleus, nucleoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 321 aa / 33.8 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=186 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=76.8; PDB: 2IPX, 7MQ8, 7MQ9, 7MQA, 7SE6, 7SE7, 7SE8 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000692, IPR020813, IPR029063; Pfam: PF01269 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **90.5/180** | |
| **归一化总分** | | | **50.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoli fibrillar center; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus, nucleolus; Nucleus, nucleoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- box C/D methylation guide snoRNP complex (GO:0031428)
- Cajal body (GO:0015030)
- extracellular exosome (GO:0070062)
- fibrillar center (GO:0001650)
- granular component (GO:0001652)
- membrane (GO:0016020)
- nucleolus (GO:0005730)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 186 |
| PubMed broad count | 3989 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FIB1, FLRN |

**关键文献**:
1. Phase separation-competent FBL promotes early pre-rRNA processing and translation in acute myeloid leukaemia.. *Nature cell biology*. PMID: 38745030
2. 2'-O-methylation at internal sites on mRNA promotes mRNA stability.. *Molecular cell*. PMID: 38906115
3. Identification of HPCAL1 as a specific autophagy receptor involved in ferroptosis.. *Autophagy*. PMID: 35403545
4. FBL promotes hepatocellular carcinoma tumorigenesis and progression by recruiting YY1 to enhance CAD gene expression.. *Cell death & disease*. PMID: 40289107
5. Elevated NPM1 and FBL expression correlates with prostate cancer aggressiveness and progression.. *The Journal of pathology*. PMID: 40705480

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.8 |
| 高置信度残基 (pLDDT>90) 占比 | 57.9% |
| 置信残基 (pLDDT 70-90) 占比 | 14.6% |
| 中等置信 (pLDDT 50-70) 占比 | 1.9% |
| 低置信 (pLDDT<50) 占比 | 25.5% |
| 有序区域 (pLDDT>70) 占比 | 72.5% |
| 可用 PDB 条目 | 2IPX, 7MQ8, 7MQ9, 7MQA, 7SE6, 7SE7, 7SE8, 7SE9, 7SEA, 7SEB |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（2IPX, 7MQ8, 7MQ9, 7MQA, 7SE6, 7SE7, 7SE8, 7SE9, 7SEA, 7SEB）+ AlphaFold极高置信度预测（pLDDT=76.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000692, IPR020813, IPR029063; Pfam: PF01269 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| tsr | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Nup153 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| BBS5 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| ENSP00000487390.1 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| MED19 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:15175163 |
| fu | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |
| MAP3K14 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RELA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TBC1D17 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| TOP1 | psi-mi:"MI:0096"(pull down) | pubmed:15848144 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.8 + PDB: 2IPX, 7MQ8, 7MQ9, 7MQA, 7SE6,  | pLDDT=76.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus, nucleolus; Nucleus, nucleoplasm / Nucleoli fibrillar center; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FBL — rRNA 2'-O-methyltransferase fibrillarin，研究基础较多，新颖性有限。
2. 蛋白大小321 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 186 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 186 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P22087
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105202-FBL/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBL
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P22087
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
