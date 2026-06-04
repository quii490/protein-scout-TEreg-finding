---
type: protein-evaluation
gene: "TEP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## TEP1 — REJECTED (研究热度过高 (PubMed strict=253，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TEP1 / TLP1, TP1 |
| 蛋白名称 | Telomerase protein component 1 |
| 蛋白大小 | 2627 aa / 290.5 kDa |
| UniProt ID | Q99973 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Vesicles; UniProt: Nucleus; Chromosome, telomere |
| 蛋白大小 | 2/10 | ×1 | 2 | 2627 aa / 290.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=253 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.0; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR056829, IPR056828, IPR025139, IPR045804, IPR007 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **68.5/180** | |
| **归一化总分** | | | **38.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Vesicles | Approved |
| UniProt | Nucleus; Chromosome, telomere | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, telomeric region (GO:0000781)
- cytoplasm (GO:0005737)
- nuclear matrix (GO:0016363)
- ribonucleoprotein complex (GO:1990904)
- telomerase holoenzyme complex (GO:0005697)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 253 |
| PubMed broad count | 374 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TLP1, TP1 |

**关键文献**:
1. Insect Hemolymph Immune Complexes.. *Sub-cellular biochemistry*. PMID: 32189298
2. Differential gene expression of human telomerase-associated protein hTERT and TEP1 in human hematopoietic cells.. *Leukemia research*. PMID: 10613358
3. Comparative gene mapping of the human and mouse TEP1 genes, which encode one protein component of telomerases.. *Genomics*. PMID: 9403057
4. PTEN/MMAC1/TEP1 in signal transduction and tumorigenesis.. *European journal of biochemistry*. PMID: 10469123
5. Genotype distribution and allele frequency of thioester-containing protein 1(Tep1) and its effect on development of Plasmodium oocyst in populations of Anopheles arabiensis in Ethiopia.. *PloS one*. PMID: 39383173

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.0 |
| 高置信度残基 (pLDDT>90) 占比 | 3.1% |
| 置信残基 (pLDDT 70-90) 占比 | 54.6% |
| 中等置信 (pLDDT 50-70) 占比 | 21.8% |
| 低置信 (pLDDT<50) 占比 | 20.5% |
| 有序区域 (pLDDT>70) 占比 | 57.7% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=67.0），有序残基占 57.7%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR056829, IPR056828, IPR025139, IPR045804, IPR007111; Pfam: PF25047, PF25048, PF13271 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NetB | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| PTEN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:24766807|imex:IM-22849 |
| Magi2 | psi-mi:"MI:0096"(pull down) | pubmed:15951562 |
| Dlg1 | psi-mi:"MI:0096"(pull down) | pubmed:15951562 |
| Mast2 | psi-mi:"MI:0096"(pull down) | pubmed:15951562 |
| Magi3 | psi-mi:"MI:0096"(pull down) | pubmed:15951562 |
| Mast1 | psi-mi:"MI:0010"(beta galactosidase complementatio | pubmed:15951562 |
| MAST3 | psi-mi:"MI:0010"(beta galactosidase complementatio | pubmed:15951562 |
| ATN1 | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |
| PPP1CA | psi-mi:"MI:0678"(antibody array) | pubmed:17274640|imex:IM-18875 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.0 + PDB: 无 | pLDDT=67.0, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus; Chromosome, telomere / Nucleoplasm; 额外: Vesicles | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. TEP1 — Telomerase protein component 1，研究基础较多，新颖性有限。
2. 蛋白大小2627 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 253 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 253 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99973
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129566-TEP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TEP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99973
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
