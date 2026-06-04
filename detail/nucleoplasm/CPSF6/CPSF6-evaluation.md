---
type: protein-evaluation
gene: "CPSF6"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CPSF6 — REJECTED (研究热度过高 (PubMed strict=152，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CPSF6 / CFIM68 |
| 蛋白名称 | Cleavage and polyadenylation specificity factor subunit 6 |
| 蛋白大小 | 551 aa / 59.2 kDa |
| UniProt ID | Q16630 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear speckles; UniProt: Nucleus; Nucleus, nucleoplasm; Nucleus speckle; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 551 aa / 59.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=152 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=64.5; PDB: 3P5T, 3P6Y, 3Q2S, 3Q2T, 4B4N, 4U0A, 4U0B |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR034772, IPR057951, IPR034769, IPR012677, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Enhanced |
| UniProt | Nucleus; Nucleus, nucleoplasm; Nucleus speckle; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- interchromatin granule (GO:0035061)
- membrane (GO:0016020)
- mRNA cleavage and polyadenylation specificity factor complex (GO:0005847)
- mRNA cleavage factor complex (GO:0005849)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 152 |
| PubMed broad count | 211 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CFIM68 |

**关键文献**:
1. Structural and mechanistic bases for a potent HIV-1 capsid inhibitor.. *Science (New York, N.Y.)*. PMID: 33060363
2. NUDT21 lactylation reprograms alternative polyadenylation to promote cuproptosis resistance.. *Cell discovery*. PMID: 40425546
3. Structure, Function, and Interactions of the HIV-1 Capsid Protein.. *Life (Basel, Switzerland)*. PMID: 33572761
4. CPSF6 promotes HIV-1 preintegration complex function.. *Journal of virology*. PMID: 40202316
5. The capsid revolution.. *Journal of molecular cell biology*. PMID: 38037430

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 64.5 |
| 高置信度残基 (pLDDT>90) 占比 | 22.5% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 29.9% |
| 低置信 (pLDDT<50) 占比 | 34.5% |
| 有序区域 (pLDDT>70) 占比 | 35.6% |
| 可用 PDB 条目 | 3P5T, 3P6Y, 3Q2S, 3Q2T, 4B4N, 4U0A, 4U0B, 4WYM, 6AY9, 6GX9 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=64.5），有序残基占 35.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034772, IPR057951, IPR034769, IPR012677, IPR035979; Pfam: PF00076, PF25524 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NUDT21 | 0.999 | 0.990 | — |
| CPSF7 | 0.996 | 0.837 | — |
| U2AF2 | 0.995 | 0.308 | — |
| CSTF2 | 0.992 | 0.400 | — |
| CPSF3 | 0.988 | 0.190 | — |
| CPSF1 | 0.987 | 0.325 | — |
| CPSF2 | 0.982 | 0.190 | — |
| CPSF4 | 0.978 | 0.190 | — |
| VIRMA | 0.969 | 0.421 | — |
| SYMPK | 0.963 | 0.374 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000391774.2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-30059|pubmed:39251607 |
| Camk2a | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| WWP1 | psi-mi:"MI:0096"(pull down) | pubmed:16189514|imex:IM-16520| |
| UBAC1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| WWP2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| NCK2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| ARMC7 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| KLHL12 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| EWSR1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| RELB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=64.5 + PDB: 3P5T, 3P6Y, 3Q2S, 3Q2T, 4B4N,  | pLDDT=64.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Nucleus, nucleoplasm; Nucleus speckle; Cy / Nucleoplasm, Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. CPSF6 — Cleavage and polyadenylation specificity factor subunit 6，研究基础较多，新颖性有限。
2. 蛋白大小551 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 152 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=64.5），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 152 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q16630
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111605-CPSF6/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CPSF6
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q16630
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
