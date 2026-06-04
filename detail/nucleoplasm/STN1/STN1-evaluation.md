---
type: protein-evaluation
gene: "STN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STN1 — REJECTED (研究热度过高 (PubMed strict=141，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STN1 / OBFC1 |
| 蛋白名称 | CST complex subunit STN1 |
| 蛋白大小 | 368 aa / 42.1 kDa |
| UniProt ID | Q9H668 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Chromosome, telomere |
| 蛋白大小 | 10/10 | ×1 | 10 | 368 aa / 42.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=141 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.1; PDB: 4JOI, 4JQF, 6W6W, 7U5C, 8D0B, 8D0K, 8SOJ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015253, IPR042082, IPR012340, IPR004365, IPR040 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Supported |
| UniProt | Nucleus; Chromosome, telomere | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- CST complex (GO:1990879)
- fibrillar center (GO:0001650)
- intermediate filament cytoskeleton (GO:0045111)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 141 |
| PubMed broad count | 287 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: OBFC1 |

**关键文献**:
1. Dyskeratosis Congenita and Related Telomere Biology Disorders.. **. PMID: 20301779
2. STN1 facilitates metastasis by promoting transcription of EMT-activator ZEB1 in pancreatic cancer.. *Nature communications*. PMID: 40841373
3. Comparison of Telomere Structure in Eukaryotes.. *Archives of Razi Institute*. PMID: 40606259
4. POT1 recruits and regulates CST-Polα/primase at human telomeres.. *Cell*. PMID: 38838667
5. The evolving genetic landscape of telomere biology disorder dyskeratosis congenita.. *EMBO molecular medicine*. PMID: 39198715

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.1 |
| 高置信度残基 (pLDDT>90) 占比 | 66.0% |
| 置信残基 (pLDDT 70-90) 占比 | 20.9% |
| 中等置信 (pLDDT 50-70) 占比 | 7.3% |
| 低置信 (pLDDT<50) 占比 | 5.7% |
| 有序区域 (pLDDT>70) 占比 | 86.9% |
| 可用 PDB 条目 | 4JOI, 4JQF, 6W6W, 7U5C, 8D0B, 8D0K, 8SOJ, 8SOK |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（4JOI, 4JQF, 6W6W, 7U5C, 8D0B, 8D0K, 8SOJ, 8SOK）+ AlphaFold极高置信度预测（pLDDT=87.1），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015253, IPR042082, IPR012340, IPR004365, IPR040260; Pfam: PF09170, PF01336 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TEN1 | 0.999 | 0.982 | — |
| CTC1 | 0.999 | 0.982 | — |
| RPA1 | 0.998 | 0.496 | — |
| RPA3 | 0.997 | 0.296 | — |
| MED23 | 0.994 | 0.994 | — |
| MED25 | 0.994 | 0.994 | — |
| MED8 | 0.994 | 0.994 | — |
| MED4 | 0.994 | 0.994 | — |
| MED30 | 0.994 | 0.994 | — |
| MED12 | 0.994 | 0.994 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TEN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:18719252 |
| Pot1b | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22748632|imex:IM-17623 |
| HTT | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| GRIN2C | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| KLF11 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |
| TUBGCP4 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Ap2m1 | psi-mi:"MI:0096"(pull down) | pubmed:14726597 |
| HMT1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| ATG12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:14690591 |
| fsR | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.1 + PDB: 4JOI, 4JQF, 6W6W, 7U5C, 8D0B,  | pLDDT=87.1, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, telomere / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. STN1 — CST complex subunit STN1，研究基础较多，新颖性有限。
2. 蛋白大小368 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 141 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 141 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H668
- Protein Atlas: https://www.proteinatlas.org/ENSG00000107960-STN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H668
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
