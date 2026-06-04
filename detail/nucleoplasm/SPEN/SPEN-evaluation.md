---
type: protein-evaluation
gene: "SPEN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## SPEN — REJECTED (研究热度过高 (PubMed strict=168，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | SPEN / KIAA0929, MINT, SHARP |
| 蛋白名称 | Msx2-interacting protein |
| 蛋白大小 | 3664 aa / 402.2 kDa |
| UniProt ID | Q96T58 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus |
| 蛋白大小 | 0/10 | ×1 | 0 | 3664 aa / 402.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=168 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v? pLDDT=0; PDB: 1OW1, 2RT5, 4P6Q, 7Z1K |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR049095, IPR049094, IPR049093, IPR012677, IPR035 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **65.0/180** | |
| **归一化总分** | | | **36.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- extracellular exosome (GO:0070062)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription repressor complex (GO:0017053)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 168 |
| PubMed broad count | 451 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0929, MINT, SHARP |

**关键文献**:
1. Large-scale targeted sequencing identifies risk genes for neurodevelopmental disorders.. *Nature communications*. PMID: 33004838
2. Systematic discovery of Xist RNA binding proteins.. *Cell*. PMID: 25843628
3. SPEN haploinsufficiency causes a neurodevelopmental disorder overlapping proximal 1p36 deletion syndrome with an episignature of X chromosomes in females.. *American journal of human genetics*. PMID: 33596411
4. SPEN integrates transcriptional and epigenetic control of X-inactivation.. *Nature*. PMID: 32025035
5. Escape from X inactivation is directly modulated by levels of Xist non-coding RNA.. *bioRxiv : the preprint server for biology*. PMID: 38559194

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v? |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 1OW1, 2RT5, 4P6Q, 7Z1K |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR049095, IPR049094, IPR049093, IPR012677, IPR035979; Pfam: PF20809, PF20808, PF20810 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NCOR2 | 0.975 | 0.622 | — |
| RBPJ | 0.973 | 0.845 | — |
| NCOR1 | 0.898 | 0.292 | — |
| MSX2 | 0.892 | 0.088 | — |
| NOTCH1 | 0.790 | 0.052 | — |
| HDAC1 | 0.739 | 0.292 | — |
| CTBP1 | 0.722 | 0.292 | — |
| CIZ1 | 0.670 | 0.000 | — |
| WTAP | 0.667 | 0.187 | — |
| CHD4 | 0.619 | 0.510 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| BCL6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:16147992 |
| ATXN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| RIDA | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| SERTAD1 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| hemD | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ENSP00000364912.3 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Q81SN0 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| A0A0F7RBH0 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 1OW1, 2RT5, 4P6Q, 7Z1K | pLDDT=0, v? | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. SPEN — Msx2-interacting protein，研究基础较多，新颖性有限。
2. 蛋白大小3664 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 168 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据暂缺

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 168 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96T58
- Protein Atlas: https://www.proteinatlas.org/ENSG00000065526-SPEN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=SPEN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96T58
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
