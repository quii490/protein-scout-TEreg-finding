---
type: protein-evaluation
gene: "FARP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## FARP2 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FARP2 / KIAA0793, PLEKHC3 |
| 蛋白名称 | FERM, ARHGEF and pleckstrin domain-containing protein 2 |
| 蛋白大小 | 1054 aa / 119.9 kDa |
| UniProt ID | O94887 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: Cytosol; UniProt: 无注释 |
| 蛋白大小 | 8/10 | ×1 | 8 | 1054 aa / 119.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=15 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.6; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019749, IPR035899, IPR000219, IPR000798, IPR014 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **111.5/180** | |
| **归一化总分** | | | **61.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

**IF 图像获取**: 尝试获取IF原图中...

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 15 |
| PubMed broad count | 47 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0793, PLEKHC3 |

**关键文献**:
1. Farp2 and Stk25 are candidate genes for the HDL cholesterol locus on mouse chromosome 1.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 18988887
2. FARP2, HDLBP and PASK are downregulated in a patient with autism and 2q37.3 deletion syndrome.. *American journal of medical genetics. Part A*. PMID: 19365831
3. Structural analyses of FERM domain-mediated membrane localization of FARP1.. *Scientific reports*. PMID: 29992992
4. Pathogenic nsSNPs that increase the risks of cancers among the Orang Asli and Malays.. *Scientific reports*. PMID: 34373545
5. Semaphorin 3A Induces Odontoblastic Phenotype in Dental Pulp Stem Cells.. *Journal of dental research*. PMID: 27302880

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.6 |
| 高置信度残基 (pLDDT>90) 占比 | 53.3% |
| 置信残基 (pLDDT 70-90) 占比 | 14.5% |
| 中等置信 (pLDDT 50-70) 占比 | 4.6% |
| 低置信 (pLDDT<50) 占比 | 27.5% |
| 有序区域 (pLDDT>70) 占比 | 67.8% |
| 可用 PDB 条目 | 无 |


**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.6，有序区 67.8%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019749, IPR035899, IPR000219, IPR000798, IPR014847; Pfam: PF08736, PF09380, PF00373 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CDC42 | 0.925 | 0.000 | — |
| SRC | 0.910 | 0.000 | — |
| RAP1A | 0.907 | 0.000 | — |
| PIP5K1C | 0.907 | 0.000 | — |
| RAP1B | 0.907 | 0.000 | — |
| PLXNA1 | 0.875 | 0.000 | — |
| PLXNA4 | 0.829 | 0.000 | — |
| SEMA3A | 0.827 | 0.000 | — |
| RAC1 | 0.773 | 0.000 | — |
| FES | 0.767 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| UBE2G2 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-15364|pubmed:21988832 |
| tdh | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| ddl | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CSNK1E | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-17578|pubmed:23455922 |
| ESR1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:31527615|imex:IM-26954 |
| PRKCZ | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:31980649|imex:IM-26434 |
| CHN1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| DNAJB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| NOC2L | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |
| VAV1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:32203420|imex:IM-26436 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.6 + PDB: 无 | pLDDT=74.6, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. FARP2 — FERM, ARHGEF and pleckstrin domain-containing protein 2，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小1054 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 15 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 深度机制分析

FARP2（UniProt O94887）属于含有FERM超家族的多结构域RhoGEF蛋白，其结构域架构从N端到C端依次为：（1）FERM结构域（B41, IPR019749），一个由F1（泛素样折叠）、F2（酰基辅酶A结合蛋白样折叠）和F3（磷酸酪氨酸结合样折叠）三叶草形模块组成，介导与磷脂酰肌醇脂质和跨膜受体的膜定位；（2）DH（Dbl homology, IPR000219）结构域，典型的RhoGEF催化核心，采用约180残基的细长螺旋束折叠，通过直接接触Rho GTPase的switch I/II区域催化GDP/GTP交换；（3）PH（pleckstrin homology, IPR000798）结构域，紧随DH结构域之后，通过结合PI(4,5)P2/PI(3,4,5)P3磷酸肌醇将DH-PH串联模块锚定至质膜，协同RhoGEF活性的膜定位；（4）C端FERM相邻结构域（IPR014847），功能未完全注释但可能参与自身抑制或额外互作。

AlphaFold v6预测pLDDT=74.6，有序区域67.8%，高置信残基53.3%——这一中等置信度反映了FARP2作为大型多结构域蛋白（1054 aa/119.9 kDa）的模块化架构特征：各结构域（FERM/DH/PH）内部折叠置信度高，而结构域间连接区（linker）因缺乏有序二级结构而呈低置信度。无实验PDB结构，但FARP1的同源FERM结构域晶体结构（PMID:29992992）提供了FERM模块膜定位机制的可靠模型。

STRING-PPI网络将FARP2置于semaphorin/plexin信号轴：CDC42（0.925）、SRC（0.910）、RAC1（0.773）为经典Rho GTPase信号节点，PLXNA1（0.875）和PLXNA4（0.829）为semaphorin受体，SEMA3A（0.827）为信号配体。IntAct实验数据提供了人类蛋白互作的直接证据：CHN1（alpha-chimaerin, RacGAP, PMID:32203420）、VAV1（Rac1 GEF, PMID:32203420）、PRKCZ（atypical PKCzeta, PMID:31980649）和CSNK1E（casein kinase 1 epsilon, PMID:23455922）均为信号转导核心因子。RAP1A/RAP1B（0.907）参与integrin-mediated cell adhesion，PIP5K1C（0.907）生成PI(4,5)P2，整条通路描绘了一个从"semaphorin→plexin→FARP2→RhoGTPase→细胞骨架/黏附"的完整信号传递链。

HPA IF仅定位到Cytosol（胞质溶胶, approved），核定位得分2/10，GO注释仅限于cytoplasm和cytosol。这一结果与FARP2的FERM-DH-PH膜靶向机制一致——FERM结构域和PH结构域对质膜磷酸肌醇的亲和力将蛋白招募至胞质膜近端，而非细胞核。FARP2的功能完全限定在细胞骨架调控和RhoGTPase信号范畴，缺乏任何核定位信号（NLS）、DNA/染色质结合结构域或核蛋白互作证据。在semaphorin 3A诱导牙髓干细胞成牙本质分化（PMID:27302880）和HDL胆固醇代谢调控（PMID:18988887）中的功能均通过胞质信号通路介导。

从TE调控筛选角度，FARP2的淘汰理由充分：核定位=2/10，远低于3分的最低阈值。其FARP2-FERM-DH-PH三模块GEF架构已被FARP1的结构研究（PMID:29992992）深入阐述，蛋白的功能范式明确限定在胞质信号转导范畴。虽然RhoGTPase信号通路间接影响染色质状态（通过SRF/MRTF转录因子和actin dynamics），但这种远端关联不符合新TE调控候选蛋白的直接靶向标准。

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O94887
- Protein Atlas: https://www.proteinatlas.org/ENSG00000006607-FARP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FARP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O94887
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O94887-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
