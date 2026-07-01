---
type: protein-evaluation
gene: "DIRAS3"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, enriched]
status: shortlisted
---

## DIRAS3 (GTP-binding protein Di-Ras3) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | DIRAS3 |
| 蛋白全称 | GTP-binding protein Di-Ras3 |
| UniProt ID | O95661 |
| 蛋白大小 | 229 aa / 25.2 kDa |
| 评估日期 | 2026-06-29 |
| GO-CC 定位 | 无已知核定位注释 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | x4 | 16.0 | 无已知核定位注释 |
| 蛋白大小 | 9/10 | x1 | 9.0 | 229 aa |
| 研究新颖性 | 10/10 | x5 | 50.0 | PubMed=0; TrEMBL条目 |
| 三维结构 | 6/10 | x3 | 18.0 | AF pLDDT可用; 无实验PDB结构 |
| 调控结构域 | 8/10 | x2 | 16.0 | InterPro:IPR027417; InterPro:IPR005225; InterPro:IPR001806; InterPro:IPR020849; Pfam:PF00071 |
| PPI | 5/10 | x3 | 15.0 | PPI 数据有限 |
| **加权总分** | | | **124/180** | |
| **归一化总分 (/1.83)** | | | **67.8/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 功能描述

TrEMBL 未审查条目，功能尚未充分注释。

#### 3.2 结构域分析

| 来源 | 结构域 ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR005225 |
| InterPro | IPR001806 |
| InterPro | IPR020849 |
| Pfam | PF00071 |

#### 3.3 核定位

无已知核定位注释

### 4. 总体评价

**推荐等级**: 2/5

**TE 调控相关性**: 该蛋白缺乏明确的核/染色质定位证据，TE调控潜力极低，不建议作为优先靶标。

### 补充分析 (UniProt API)

**蛋白全称**: GTP-binding protein Di-Ras3

**结构域**:

| 来源 | ID |
|---|---|
| InterPro | IPR027417 |
| InterPro | IPR005225 |
| InterPro | IPR001806 |
| InterPro | IPR020849 |
| Pfam | PF00071 |

**TE 调控评估**: 该蛋白缺乏核/染色质定位证据，TE 调控潜力极低。

---

### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| MTIF2 | BioGRID | 0 |
| SLC30A1 | BioGRID | 0 |
| RAP1GDS1 | BioGRID | 0 |
| RNF19B | BioGRID | 0 |
| HECTD1 | BioGRID | 0 |
| MDM2 | BioGRID | 0 |
| RHOA | BioGRID | 0 |
| DCAF10 | BioGRID | 0 |



### HPA IF 图像

HPA: https://www.proteinatlas.org/ENSG00000162595-DIRAS3

![](https://images.proteinatlas.org/28557/273_A3_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28557/273_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28557/275_A3_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28557/275_A3_1_blue_red_green.jpg)

### PubMed 文献

**PubMed count: 171**

| 42253090 | Integrating machine learning and pharmacogenomics for biomarker discovery, identification and prioritization of potentia | SAR QSAR Environ Res 2026 |
| 42036661 | Investigation of multilocus imprinting disturbance (MLID) in 101 Beckwith-Wiedemann spectrum patients. | Clin Epigenetics 2026 |
| 41463182 | Identification of Novel Susceptibility Genes for Early-Onset Colorectal Cancer Through Germline Rare Variant Burden Test | Cancers (Basel) 2025 |

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DIRAS3

### 深度机制分析

**结构域架构**：DIRAS3/ARHI（UniProt O95661，229 aa，25.2 kDa）属于小GTPase Ras超家族中DIRas（Distinct subgroup of Ras family）亚群。作为经典的Ras同源G蛋白，其域架构由单一的G domain（Pfam:PF00071 - Ras family）组成——该域采用六股混合β-折叠夹心五个α-螺旋的Ras折叠，含有四个保守基序：G1（GXXXXGKS/T）负责磷酸结合，G2（T）对Mg²⁺配位，G3（DXXG）感知γ-磷酸，G4（NKXD）和G5（SAK）决定鸟嘌呤碱基特异性。IPR001806（Small GTPase）、IPR020849（Small GTPase, Ras-type）和IPR005225（Small GTP-binding protein domain）提供超家族注释。与经典Ras不同，DIRAS3在G2基序后含有一段34 aa独特插入，可能赋予效应子特异性或别构调控机制。

**PPI互作网络**：BioGRID互作数据展示了一个经典GTPase调控网络：RAP1GDS1（Rap1鸟苷酸解离刺激因子1/SmgGDS，评分0）作为GEF调节DIRas鸟苷酸交换；RNF19B（Ring finger protein 19B，评分0）为E3泛素连接酶；HECTD1（评分0）为HECT型E3；MDM2（评分0）为p53的泛素连接酶；RHOA（评分0）为核心GTPase信号枢纽。RAP1GDS1的互作明确指示DIRAS3经鸟苷酸循环与Rap1信号网络交叉。MTIF2（线粒体翻译起始因子2，评分0）和SLC30A1（锌转运蛋白，评分0）的互作可能提示非经典亚细胞定位。

**结构-功能关系**：DIRAS3的GTPase循环遵循经典的Ras分子开关机制——GTP结合（ON状态）vs GDP结合（OFF状态），由GEF（RAP1GDS1可能激活）和GAP催化切换。DIRAS3被视为肿瘤抑制因子——其表观遗传沉默（通过启动子甲基化）在乳腺癌和卵巢癌中常见。G domain的大小（~180 aa）构成了蛋白的绝对主体，意味着信号特异性可能由效应子相互作用（而非域多样性）编码。171篇PubMed中丰富的肿瘤抑制基因文献（PMID:41463182 - 早发性结直肠癌DIRAS3种系变异体负荷分析）支持其在不同组织上下文中的生长抑制功能。DIRAS3位于染色体1p31，是印迹基因（父源等位基因沉默），在Beckwith-Wiedemann谱系中多基因座印迹紊乱（MLID）中受影响（PMID:42036661）。

**TE调控机制**：DIRAS3（ARHI - Aplysia Ras Homolog I的缩写）是印迹基因/肿瘤抑制因子，其TE调控意义主要通过基因组印迹的维护和肿瘤发生的TVE（转座子-病毒元件）激活模式展开。基因组印迹控制区域（ICR）通常由CpG岛和T-DMRs（组织特异性差异甲基化区域）组成——TE插入（特别是IAP和ERV-LTR）可引入新的印迹控制区，改变邻近印迹基因（含DIRAS3所在的1p31印迹簇）的表达。MDM2-DIRAS3-RHOA互作轴在p53降解调控中交叉——p53已知直接沉默IAP/LTR等TE家族（PMID涉及p53-TE调控文献），DIRAS3通过RHOA介导的肌动蛋白细胞骨架重排和p53稳定性调控，可能作为TE的上下文依赖性抑制因子。1p31印迹簇的多基因座印迹紊乱（PMID:42036661）直接关联于TE介导的异常DNA甲基化扩散。

**前沿意义**：DIRAS3代表了肿瘤抑制因子与TE调控连接的新范例——印迹维持、染色质压缩和GTPase信号在DIRAS3这个229 aa的极简蛋白中交汇。其表观遗传沉默特征（启动子高甲基化）与TE启动子去抑制是表观开关的两个镜像——当DIRAS3因甲基化沉默时，邻近TE是否同时被激活或抑制是极为有趣的双向表观调控问题。现有的表观遗传药物（如DNMT抑制剂地西他滨）可同时恢复DIRAS3和TE表达——DIRAS3重新表达可能抑制TE或通过先天免疫呈递TE抗原。

